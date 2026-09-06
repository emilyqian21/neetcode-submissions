class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp definition:
        # dp[i][j] = minimum steps to turn word1[:i] into word2[:j]
        # main logic:
        # 1） 如果最后一个字符相等，那就什么都不用做
        #     dp[i][j] = dp[i - 1][j - 1]
        # 2） 如果最后一个字符不相等，那就要min(insert, delete, replace)
        # insert: w1 = "ab", w2 = "abc" 
        #         dp[i][j] = dp[i][j - 1] + 1 
        #         因为insert c之后，问题就变成 w1"ab" 变成w2“ab"需要几步
        # delete: w1 = "abcd", w2 = "abc"
        #         dp[i][j] = dp[i - 1][j] + 1
        #         因为delete d之后，问题就变成了 w1"abc" 变成 w2"abc"需要几步
        # replace: w1 = "abd", w2 = "abc"
        #          dp[i][j] = dp[i - 1][j - 1] + 1
        #          因为replace d 之后，问题就变成了 w1"ab"变成w2"ab"需要几步
        # 最后，dp = min(insert, delete, replace )

        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]* (n2 + 1) for _ in range(n1 + 1)]

        # base case
        for i in range(n1 + 1): 
            dp[i][0] = i # w2 = ""
        for j in range(n2 + 1):
            dp[0][j] = j # w1 = ""
        
        # main logic
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete_option = dp[i - 1][j] + 1
                    insert_option = dp[i][j - 1] + 1
                    replace_option = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(delete_option, insert_option, replace_option)
        return dp[-1][-1]
