class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2 

            if nums[m] > nums[r]: # in large array, m can't be the answer
                l = m + 1

            else: # in small array, m can be the answer
                r = m 

        return nums[l] # l == r