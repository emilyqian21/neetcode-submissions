class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ## Time: O(n * m)
        # We calculate every combination of prefixes of s1 and s2.

        # Space: O(n * m)  --> 可以optimize 成 O（min(n,m))
        # We use a 2D DP table with n * m states. 
        n = len(s1)
        m = len(s2)

        #edge case
        if n + m != len(s3):
            return False
        
        dp = [[False] * (n + 1) for _ in range(m+1)] # row is s1, column is s2; dp[i][j] = s1[:i] + s2[:j] can form s3[:i + j]
        dp[0][0] = True # there is 1 way to form "" from s1 and s2

        for c in range(1, n + 1):
            dp[0][c] = dp[0][c-1] and s3[c-1] == s1[c - 1]
        for r in range(1,m + 1):
            dp[r][0] = dp[r - 1][0] and s3[r-1] == s2[r-1]

        for r in range(1,m + 1):
            for c in range(1,n + 1):
                # use row (s1) or  use column(s2)
                dp[r][c] = (dp[r][c-1] and s1[c - 1] == s3[ r+ c - 1]) or (dp[r - 1][c] and s3[r + c - 1] == s2[ r - 1])
        return dp[-1][-1]
                
