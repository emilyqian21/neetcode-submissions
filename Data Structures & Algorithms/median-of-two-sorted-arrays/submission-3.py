class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        short = nums1 
        long = nums2

        total = len(short) + len(long)
        half = total // 2

        l = 0 
        r = len(short) # 因为 i 是“左边元素个数”，所以它可以等于 len(short)。
        while l <= r:      
            # i = num of elements in short left, j = num of elements in short right 
            i = (l + r) // 2
            j = half - i

            short_left = short[i - 1] if (i - 1) >= 0 else -float('inf')
            short_right = short[i] if i < len(short) else float('inf') 
            long_left = long[j - 1] if (j - 1) >= 0 else -float('inf')
            long_right = long[j] if j < len(long) else float('inf')

            if short_left <= long_right and long_left <= short_right:
                # odd
                if total % 2 == 1:
                    return min( short_right, long_right)
                # even
                else:
                    return (max(short_left, long_left) + min(short_right, long_right) ) / 2
            elif short_left > long_right: # too many elements in short
                r = i - 1
            else:
                l = i + 1
            


