class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, open_n, close_n):
            if open_n == close_n == n:
                res.append(''.join(path))
                return
            if close_n > open_n:
                return
            if open_n > n:
                return 

            # choose 
            path.append("(")
            # explore
            dfs(path, open_n + 1, close_n)
            # undo
            path.pop()

            # choose
            path.append(")")
            # explore
            dfs(path, open_n, close_n + 1)
            # undo
            path.pop()

            return
        dfs([], 0, 0)
        return res
