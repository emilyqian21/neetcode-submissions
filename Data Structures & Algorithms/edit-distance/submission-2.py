class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # time: O (m * n)
        # space: O( m * n)
        len_w1 = len(word1)
        len_w2 = len(word2)

        dp = [ [0] * (len_w2 + 1)    for _ in range(len_w1 + 1)] # dp[r][c] = minium steps to turn w1[:r] to w2[:c]

        # base case
        for r in range(len_w1 + 1):
            dp[r][0] = r  # minimum steps to turn w1[:r] to w2[:0]
        for c in range(len_w2 + 1):
            dp[0][c] = c # minimum steps to turn w1[:0] to w2[:c]

        for r in range(1, len_w1 + 1):
            for c in range(1, len_w2 + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    delete = dp[r - 1][c] + 1 
                    insert = dp[r][c - 1] + 1
                    replace = dp[r - 1][c - 1] + 1
                    dp[r][c] = min(delete, insert, replace)
        return dp[-1][-1]