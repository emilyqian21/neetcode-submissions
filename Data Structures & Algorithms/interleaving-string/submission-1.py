class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # time: O(len_s1 * len_s2)， 2 for loops
        # space： O(len_s1 * len_s2), grid
        len_s1 = len(s1)
        len_s2 = len(s2)
        dp = [ [False] *(len_s2 + 1)   for _ in range(len_s1 + 1)] # dp[i][j] = can we using s1[:i] and s2[:j] to get s3[:i+j]?
        # edge case
        if len_s1 + len_s2 != len(s3):
            return False
        # first value 
        dp[0][0] = True # we can using s[:0] ="" and s2[:0]"" to get s3[:0]""

        # first row(s1[0]),every column (every value in s2)
        for c in range(1,len_s2 + 1):
            dp[0][c] = dp[0][c-1] and s2[c-1] == s3[c-1]   # dp[0][1], dp[0][2],dp[0][3]
        for r in range(1, len_s1 + 1):
            dp[r][0] = dp[r-1][0] and s1[r-1] == s3[r-1]  # dp[1][0], dp[2][0],dp[3][0]
        
        #now loop thru each value in s1 and s2 execpt the first value
        for r in range(1, len_s1 + 1): #dp[1][c] dp[2][c] dp[3][c]
            for c in range(1,len_s2 + 1): #dp[r][1] dp[r][2] dp[r][3]
                dp[r][c] = (dp[r-1][c] and s1[r-1] == s3[r-1+c]) or ( dp[r][c-1] and s2[c-1] == s3[ r+c-1])
                # dp[r][c] 意味着can we using s1[:i] and s2[:j] to get s3[:i+j]? 
                # dp[r][c] 只有两种情况，就是这一次用s1 或者这一次用 s2
        return dp[-1][-1]
         
