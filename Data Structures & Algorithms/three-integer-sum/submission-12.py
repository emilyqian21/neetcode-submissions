class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # deduplicate
                continue
            target = -nums[i]
            # two pointers
            l = i + 1
            r = len(nums) - 1
            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum == target:
        
                    res.append([nums[i], nums[l] ,nums[r]])
                    l += 1
                    r -= 1
       
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                elif cur_sum < target:
                    l += 1
                else:
                    r -= 1
              
        return res

