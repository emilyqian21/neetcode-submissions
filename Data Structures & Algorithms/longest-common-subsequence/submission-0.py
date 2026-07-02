class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #time: O(n × m)
        #space: O(n × m)
        n = len(text1)
        m = len(text2)

        dp = [[0]*(m+1) for _ in range(n+1)] #dp[i][j] = at text1[:i] and text2[:j], how many characters are the same --> what is longest common subsequence so far

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]: # at text1[:i] --> last character is text1[i-1]
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
        return dp[-1][-1]
        
        #space optimized version
        # Space O(m)
        # n, m = len(text1), len(text2)

        # dp = [0] * (m + 1)

        # for i in range(1, n + 1):
        #     prev_diag = 0  # stores dp[i-1][j-1]
        #     for j in range(1, m + 1):
        #         temp = dp[j]  # store old dp[i-1][j]

        #         if text1[i - 1] == text2[j - 1]:
        #             dp[j] = 1 + prev_diag
        #         else:
        #             dp[j] = max(dp[j], dp[j - 1])

        #         prev_diag = temp

        # return dp[m]