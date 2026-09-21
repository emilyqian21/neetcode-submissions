class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # definition: 
        # dp[i][j] = number of ways to use s[:i] to form t[:j]. last character s[i - 1] and t [j - 1]
        # main logic:
        # three cases --> 
        # 1) current character of s == current chracter of t
        #   1.1) choose not to use the current character of s 
        #   1.2） and choose to use it 
        #   dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] 
        #   num of ways to use s[:i] to form t[:j] = num of ways to use s[:i - 1] to form t[:j] and number of ways to use s[:i - 1] to form t[:j - 1]
     
        # 2) current character of s != current chracter of t  ---> s[i - 1] != t[j - 1]
        #    can't use the current character of s
        #    dp[i][j] = dp[i - 1][j]


        n1 = len(s)
        n2 = len(t)
        # edge case
        if n1 < n2:
            return 0

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # base case 单独处理 比较干净
        for i in range(n1 + 1): # t = ""永远只有一种方式合成
            dp[i][0] = 1  
            # 为什么不需要写 for j in range(n2 + 1), dp[0][j] = 0? 
            # 因为 source 为空但 target 不为空 → 0 种方法, 已经在dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]写过了

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                if s[i - 1] != t[j - 1]:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
