class Solution:
    def search(self, nums: List[int], target: int) -> int:
            # 1. find the pivot
            l = 0 
            r = len(nums) - 1

            while l < r: # l == r is when we find the pivot
                m = l + (r-l)//2
                if nums[m] > nums[r]: # we are at the big part, l can't be the answer
                    l = m + 1
                else:  # we are at the small part and r can be the answer
                    r = m
                
            pivot = l 


            def binary_search(left,right):
                while left <= right:
                    mid = left + (right - left)//2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1 
                return -1

            left_result = binary_search(0,pivot -1)
            if left_result != -1:
                return left_result
            right_result = binary_search(pivot,len(nums)-1)
            return right_result
            #time: O(log n)
            #space: O(1)
