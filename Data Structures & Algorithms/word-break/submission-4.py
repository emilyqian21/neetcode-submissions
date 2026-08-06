class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict = set(wordDict) # set loopup is O(1), list is O(n)
        # n = len(s)
        # dp = [False] * (n + 1) # prefix
        # dp[0] = True # we can use 0 word in wordDict to form string

        # for i in range(1, len(dp)):
        #     for j in range(i):
        #         if dp[j] and s[j:i] in wordDict:
        #             dp[i] = True
        #             break # no need to further explore j
        # return dp[-1]

        wordDict = set(wordDict) # set loopup is O(1), list is O(n)
        n = len(s)
        dp = [False] * (n + 1) # prefix
        dp[0] = True # we can use 0 word in wordDict to form string
        true_idx = [0]

        for i in range(1, len(dp)):
            for j in true_idx:
                if s[j:i] in wordDict:
                    dp[i] = True
                    true_idx.append(i)
                    break # no need to further explore j
        return dp[-1]