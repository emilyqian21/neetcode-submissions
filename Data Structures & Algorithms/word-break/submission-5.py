class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        def dfs(s):
            # if s can be segmented into wordict
            if not s:
                return True
            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1): # s[0:i] s[0:1], s[0:2], s[0:8], last character s[i - 1]
                if s[:i] in wordDict:
                    res = dfs(s[i:])
                    memo[s] = res
                    if res:
                        return True
            memo[s] = False
            return False
        
        return dfs(s)