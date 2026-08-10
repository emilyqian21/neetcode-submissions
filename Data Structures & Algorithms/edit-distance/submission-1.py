class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # time: O(len_w1 * len_w2)
        # space: O(len_w1 * len_w2) ---> 可以用1d 写法 optimize 成 O（len_w2)
        len_w1 = len(word1)
        len_w2 = len(word2)
        #把dp[i][j] = 把 word1[:i] 变成 word2[:j] 所需要的最少操作次数
        dp = [ [0] *(len_w2 + 1) for _ in range(len_w1 + 1) ] # dp[i][j] = the mininal steps to turn word1[:i] into word2[:j] 
        dp[0][0] = 0 # the minimal steps to turn word1[:0] "" into word2[:0]"" is 0

        for r in range(1,len_w1 + 1): #第一列：把 word1[:r] 变成 ""，只能一直 delete。
            dp[r][0] = r # the minimal steps to turn word1[:r] "" into word2[:0]"" is deleting 0:r-1 characters, total r chars
        for c in range(1, len_w2 + 1): 
            dp[0][c] = c # the minimal steps to turn word1[:0]"" into word2[:c] is adding c-1 characters

        for r in range(1, len_w1 + 1):#第一行：把 "" 变成 word2[:c]，只能一直 insert。 #dp[1][], dp[2][],dp[3][]
            for c in range(1, len_w2 + 1): # dp[][1], dp[][2], dp[][3]
                # 字符相等的时候，其实还有一个"第四种选择"：什么都不做。
                if word1[r-1] == word2[c-1]: # dp[r][c] 是处理 w1[:r] w2[:c]，所以处理的最后一个字符是w1[r-1] w2[c-1]
                    dp[r][c] = dp[r-1][c-1]
                else:
                    # delete:   w1[:r-1] = roc, w1[:r] = rocc,   w2[:c] =roc, delete w1[r],delete = word1 少一个
                    delete_choice = dp[r-1][c] + 1
                    # insert:  ro    ro |c   dp[r][c-1] means minimal steps to turn w1[:r] into w2[:c-1], dp[r][c] means minal steps to turn w1[:r] into w2[:c]
                    insert_choice = dp[r][c-1] + 1 # insert = word2 少一个

                    # replace: ro | a   ro | c    dp[r-1][j-1] works, a
                    replace_choice = dp[r-1][c-1] + 1

                    dp[r][c] = min(delete_choice, insert_choice, replace_choice)
        return dp[-1][-1]


#         ""   r   o   s （word 2)
# ""       0   1   2   3
# h        1
# o        2
# r        3
# s        4
# e        5