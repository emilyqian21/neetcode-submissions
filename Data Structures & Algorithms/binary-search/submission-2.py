class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        if not nums:
            return -1

        while l <= r:
            mid = l + ((r-l)//2) #(l+r)//2 

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

        #time: O(n)
        #space: O(1)