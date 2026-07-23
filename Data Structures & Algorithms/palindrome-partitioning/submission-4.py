class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(word): # return true or false
            # edge case
            if not word:
                return True
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        res = []
        path = []

        def dfs(s):

            # base case
            if not s:
                res.append(path.copy())
                return 
            # if len("".join(path)) == len(s): # this will incur error b/c we change s
            #     res.append(path.copy())
            #     return
            

            for start in range(1,len(s) + 1): # 整个单词本身也可能是palindrome
                left_part = s[:start]
                if ispalindrome(left_part):
                    path.append(left_part)
                    # continue to right
                    dfs(s[start:]) # change s
                    # undo
                    path.pop() # undo一定是和append在同一个层级的

        dfs(s)
        return res
            # # make the choice
            # left_part = s[start: parition_idx]
            # right_part = s[partition_idx:]
            # if ispalindrome(left_part):
            #     # record current path
            #     path.append(left_aprt)
            #     # continue this path, continue partition in right_part
            #     for new_start in range(start + 1, len(s)):
            #         for new_parition_idx in range( new_start + 1, len(s)):
            #             dfs(new_start, new_partition)
            