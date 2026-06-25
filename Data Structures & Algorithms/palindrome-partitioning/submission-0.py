class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispalindrome(s):
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start,path):
            # record answer when necessary: when start == len(s)
            if start == len(s):
                res.append(path.copy())
                return
            
            # explore all possibilities
            # make decision
            for i in range(start,len(s)):
                if ispalindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    #further extend the path by exploring other following options
                    dfs(i+1,path)

                    # undo the choice
                    path.pop()
            return
        dfs(0,[])
        return res