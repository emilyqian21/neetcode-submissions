class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # time: O(n)
        # space: O(1)
        # compare three: nums[i], nums[i]*cur_max, nums[i]*cur_min
        cur_max = nums[0]
        cur_min = nums[0]
        res_max = nums[0]

        for i in range(1, len(nums)):
            temp_max = cur_max
            cur_max = max(nums[i], nums[i]*temp_max, nums[i]*cur_min)
            cur_min = min(nums[i],nums[i]*temp_max, nums[i]*cur_min)
            res_max = max(cur_max, res_max)
        return res_max