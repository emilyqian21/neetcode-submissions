class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(start, path, open_n, close_n):
            # traverse all possible path start at s[start:]
            # base case
            if start == n*2 and open_n == close_n: # traverse all position and valid
                res.append(''.join(path.copy()))
                return
            if start == n*2:
                return
            
            # main logic
            # choice space
            for c in ["(",")"]:
               
                if c == "(":
                    # make choice
                    if open_n + 1 < close_n: # invalid
                        return 
                    path.append(c)
                    dfs(start + 1, path, open_n + 1, close_n)
                    path.pop()
                else:
                    # make choice
                    if open_n < close_n + 1:
                        return 
                    path.append(c)
                    dfs(start + 1, path, open_n, close_n + 1)
                    path.pop()
            return res
        
        dfs(0,[],0,0)
        return res

                
                