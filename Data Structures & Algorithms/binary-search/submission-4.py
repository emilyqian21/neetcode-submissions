class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pattern: o(logn) search, sorted array
        # solution: binary search

        # time: O(logn)
        # space: O(1)
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r)//2  # how to prevent overflow: l + (r-l)//2
            if nums[m] == target:
                return m 
            elif nums[m] < target:
                l += 1
            else:
                r -= 1
        return -1