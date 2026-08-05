class Solution:
    def rob(self, nums: List[int]) -> int:
        # time: O(n)
        # spcae: O(1)
        def helper(s):
            n = len(s)
            if n == 0:
                return 0 
            if n == 1:
                return s[0]
            if n == 2:
                return max(s[0],s[1])
            pre = s[0] # 2 steps back 
            curr = max(s[0],s[1]) # 1step back

            for i in range(2,n):
                pre, curr = curr, max(pre + s[i], curr)
            return curr
        # edge case
        len_n = len(nums)
        if not len_n:
            return 0
        if len_n == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:])) # 易错点：nums[5], nums[:-1]为[], nums[1:]为[]