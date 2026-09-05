class Solution:
    def numDecodings(self, s: str) -> int:
        # time: O(n)
        # space: O(n) # can be minimized to O(1)
        n = len(s) 
        dp = [0] * ( n + 1)
        dp[0] = 1 #  dp[0] -> the number of ways of s[:0], --> "" --> only have one way to decode an empty string
        # dp[i] = the number of ways to decode the first i characters of the string (s[:i]).last character is s[i - 1]
       
        if not s or s[0] == "0":
            return 0
        for i in range(1, len(dp)):
            if s[i - 1] != "0": 
                dp[i] += dp[i - 1] # previous ways for sure
                print(i, s[i - 1], dp[i], dp[i - 1])
            if i >= 2 and (s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] in "0123456")):
                
                dp[i] += dp[i - 2] #If the last two digits form a valid letter (10–26), then every valid decoding of the prefix before those two digits can be extended by treating these two digits as one letter
        return dp[-1]