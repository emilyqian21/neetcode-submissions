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
            
            # make choice
            if open_n + 1 >= close_n: # invalid
                path.append("(")
                dfs(start + 1, path, open_n + 1, close_n)
                path.pop()
    
            # make choice
            if open_n >= close_n + 1:
                path.append(")")
                dfs(start + 1, path, open_n, close_n + 1)
                path.pop()
                
            return res
            
        dfs(0,[],0,0)
        return res

                
                