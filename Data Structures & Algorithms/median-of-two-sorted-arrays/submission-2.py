class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # time: O(log(min(n,m)))
        # space: O(1)

        # choose smaller nums list as A, the longer as B
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        # calculate total and half for the partition 
        total = len(A) + len(B)
        half = total // 2

        # do binary search on the short list A
        l = 0
        r = len(A) - 1
        
        while True : # why it's true not l <=r ?? 因为一定有答案； 写while l <= r 也行
            mid_a = (l + r)//2
            mid_b = half - (mid_a + 1) -1 # half -mid_a -2
            #test if our partition is valid 
            # test standard: if left_a <= right_b, left_b <= right_A, then valid
            left_part_a = A[mid_a] if mid_a >= 0 else -float('inf')
            left_part_b = B[mid_b] if mid_b >= 0 else -float('inf')
            right_part_a = A[mid_a + 1] if mid_a + 1 < len(A) else float('inf')
            right_part_b = B[mid_b + 1] if mid_b + 1 < len(B) else float('inf')

            if left_part_a <= right_part_b and left_part_b <= right_part_a:
                # parititon is valid, next we need to find the medium
                # odd
                if total % 2: 
                    res = min(right_part_a, right_part_b)
                # even
                else:
                    res = (max(left_part_a, left_part_b) +  min(right_part_a, right_part_b) )/ 2
                return res
            
            elif left_part_a > right_part_b: # too many elements from a, need to reduce
                r = mid_a - 1
            else:
                l = mid_a + 1

