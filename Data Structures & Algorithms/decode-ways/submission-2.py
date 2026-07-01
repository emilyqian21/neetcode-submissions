class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = [0] *(n + 1) # dp[i] = number of ways to decode for every prefix length
        dp[0] = 1 #The empty string has one way to decode: do nothing.
        #dp[2] --> How many ways are there to decode the substring s[0:2]
        """
        String:   2   2   6
        Index:    0   1   2
        dp[0] = ways to decode 0 characters = the empty string "", prefix = "0
        dp[1] = ways to decode 1 character = "2", prefix = "2"
        dp[2] = ways to decode 2 characters = "22", prefix = "22"
        """
        #edge case
        if not s or s[0] == "0":
            return 0

        for i in range(1, len(dp)):
            # one digit
            if s[i-1] != "0": # s[i-1] is the number before current number; if the number before current number is not 0
                dp[i] += dp[i-1] # the ways to decode before current number = ways to decode 1 digit before current number 
            #two digit
            if i >= 2 and ((s[i-2] =="1") or (s[i-2] == "2" and s[i-1] in "0123456")):
                dp[i] += dp[i-2]
        return dp[-1]