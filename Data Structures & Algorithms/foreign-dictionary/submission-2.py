class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # topological sort ( postorder dfs?)

        word2neighbor = { c: set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            # edge case
            if w1[:minlen] == w2[ :minlen] and len(w1) > len(w2):
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    word2neighbor[w1[j]].add(w2[j]) # find the first different character
                    break 


        # topolocigal sort
        status = {} # True = visited and in the loop  # False = visited but not in the loop
        output = []
        def dfs(c):
            # base case
            if c in status:
                return status[c] # return the recorded status. if status[c] == True, 说明是loop
            
            # process current node 
            status[c] = True 

            for nei in word2neighbor[c]:
                if dfs(nei):
                    return True


            status[c] = False
            output.append(c)
            return False
        
        for c in word2neighbor: # 易错点：遍历的是dict的key
            if dfs(c):
                return ""

        return "".join(output[::-1])