class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}
        def dfs(n):
            # return the minial steps to reach step n 
            if n in memo:
                return memo[n]
        
            # main logic
            cur =  dfs(n - 1) + dfs(n - 2)
            memo[n] = cur
            return cur
        return dfs(n)

