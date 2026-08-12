class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        # sort array 
        nums.sort()

        res = []
        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue # deduplicate
            
            target = - nums[i]
            
            
            # binary search two sum 
            l = i + 1
            r = n - 1

            while l < r:
                cumsum = nums[l] + nums[r]

                if cumsum == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif cumsum > target:
                    r -= 1
                else:
                    l += 1

        return res