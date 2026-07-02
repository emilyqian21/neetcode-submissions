class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # time: O(N)
        # space: O(1)
        res = nums[0]
        cur_max = 1
        cur_min = 1

        for n in nums:
            temp_max = cur_max
            cur_max = max(cur_max * n, cur_min *n, n)
            cur_min = min(temp_max * n, cur_min *n, n) # extend previous max, extend previous min,start a new subarray
            res = max(res, cur_max)
        return res

