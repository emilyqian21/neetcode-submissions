class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # solution: DP
        # dp definition:
        # dp[i] = if s[:i] can be segmented into words from wordDict
        #
        # main logic:
        # try every previous cut position j
        # if s[:j] is valid and s[j:i] is a word, then s[:i] is valid
    
        # transition:
        # dp[i] = True if there exists j < i such that:
        # dp[j] == True and s[j:i] in wordDict

        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1) #dp[0]...dp[n]

        #base case
        dp[0] = True # s[:0] = "" can be segmented into words from wordDict, because we need 0 word from wordDict
 
        for i in range(1, n + 1):
            for j in range(i): # s[j:i] --> s[0:i]...s[i - 1, i]
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]