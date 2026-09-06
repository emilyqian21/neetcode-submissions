class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # definition:
        # dp[i][j] = can we use s1[:i] and s2[:j] to form s3[:i+j]
        # main logic:
        # dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        # or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        # 即最后一个字符来自s1 或者来自s2

        n1 = len(s1)
        n2 = len(s2)
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)] # col -> n2, row -> n1
        # edge case
        if len(s1) + len(s2) != len(s3):
            return False

        dp[0][0] = True # we can use "" and "" to form ""
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0: #s1 = ""
                    dp[i][j] = (s2[:j] == s3[:j])
                elif j == 0:
                    dp[i][j] = (s1[:i] == s3[:i])
               
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        
        
        return dp[-1][-1]