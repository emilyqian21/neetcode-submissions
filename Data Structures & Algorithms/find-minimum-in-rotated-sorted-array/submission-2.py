class Solution:
    def findMin(self, nums: List[int]) -> int:
    # find the element that smaller than the left, larger than the right

        l = 0
        r = len(nums) - 1

        while l < r: # cuz we didn't remove m , we use r = m
            m = (l + r) //2 # l + (r-l)//2
            if nums[m] < nums[r]:  # answer lies in [l ... m]
                r = m 
            else:
                l = m + 1 # answer lies in [m+1 ... r], m can't be the answer
        return nums[l]

