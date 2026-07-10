class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo - start fresh, or continue this path
        # time: O(n)
        # spaceL O(1)
        glo_max = nums[0]
        cur_sum = nums[0]
        for n in nums[1:]:
            cur_sum = max(cur_sum + n, n) # start fresh, or continue current path
            glo_max = max(cur_sum, glo_max)
        return glo_max