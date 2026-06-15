class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        s = 0

        res = []
        while s < len(nums)-2:
            if nums[s]>0:
                break 
            if s >0 and nums[s] == nums[s-1]: #跳过重复的s
                s += 1
                continue
            l = s + 1
            r = len(nums) -1 

            while l < r:
                two_sum_target = 0 - nums[s]
                two_sum = nums[l] + nums[r]

                if  two_sum == two_sum_target:
                    res.append([nums[s],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:#跳过重复的L 
                        l += 1
                    while l < r and nums[r] == nums[r+1]:#跳过重复的R
                        r -= 1
                
                elif two_sum < two_sum_target:
                    l += 1
                else:
                    r -= 1
            s += 1

        return res

        #time: O(N^2)，排序 O（nlogn),两次while O(n^2), 总共O(n log n + n²)，简化为O（n^2)
        #space: O(1)