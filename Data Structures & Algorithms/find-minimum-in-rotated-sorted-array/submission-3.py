class Solution:
    def findMin(self, nums: List[int]) -> int:
    # pivot 永远位于小数区的最左端，
    # 所以只需要判断 mid 在大数区还是小数区，就能决定搜索方向。
    # 不像 Search in Rotated Sorted Array，那题还需要判断 target 是否属于当前有序区间。 
        l = 0 
        r = len(nums) -1 

        while l < r: #因为答案就是 l == r 的时候
            mid = l + (r-l)//2

            if nums[mid] < nums[r]: # 在小数区,单调递增，那么最小的数可能是MID 也可能是mid左边
                r = mid 
            else: # 当nums[mid] == nums[r]不可能因为无重复数字，所以只有nums[mid] > nums[r]，在大数区，最小的数在mid右边
                l = mid + 1

        return nums[l]
        # time: 0(log n )
        # space: O(1)

