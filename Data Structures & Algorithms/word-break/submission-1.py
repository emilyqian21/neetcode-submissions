class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1) # dp[i] means if s[:i] can be broken into worddict?
        dp[0] = True # dp[0] --> ""，空string 可以broken into worddict

        #set找的速度是O(1)， list是O(N)，所以转成set
        wordDict = set(wordDict)

        for i in range(1,len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict: # 如果s[:j]是true，可以被找到，然后剩下的部分 s[j:i]也能被找到，那么就是可以
                    dp[i] = True # 我已经找到一种方法证明 s[:i] 可以切分，不用继续尝试其他 j 了。
                    break # 不用找其他k了，接着下一个i
        return dp[-1] #最后一个i就是看整个s是否能被break