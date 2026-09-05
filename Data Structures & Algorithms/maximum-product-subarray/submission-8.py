class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's algo
        cur_max = nums[0]
        cur_min = nums[0]
        res_max = nums[0]

        for i in range(1,len(nums)):
            temp_max = cur_max
            temp_min = cur_min
 
            cur_max = max(temp_max * nums[i], temp_min * nums[i], nums[i])
            cur_min = min(temp_max * nums[i], temp_min * nums[i], nums[i])

            res_max = max(cur_max, res_max)
         
        return res_max