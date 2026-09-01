class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispalindrome(w):
            l = 0 
            r = len(w) - 1
            while l < r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(path, word):
            # return all possible scnearios for partition of word. historical path is in path, not include current node
            print(word)
            if not word: 
                res.append(path.copy())
                return
            
            for i in range(len(word)): # i = 0 
                # choose
                if not ispalindrome(word[:i + 1]):
                    continue
                path.append(word[:i + 1]) # path = ["a"]
                # explore
                dfs(path,word[i + 1:]) # dfs(["a"], [])
                # undo
                path.pop()
            return 
        dfs([], s)
        
        return res