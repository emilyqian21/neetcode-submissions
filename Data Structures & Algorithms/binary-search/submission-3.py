class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2  # how to prevent overflow
            if nums[m] == target:
                return m 
            elif nums[m] < target:
                l += 1
            else:
                r -= 1
        return -1