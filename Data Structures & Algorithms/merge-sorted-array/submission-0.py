class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # three pointers.
        # one write pointer, start at the end of nums1  1,2,3,0,0,0 <- pointer 3
        # one traverse pointer, start at the end of non-zero values of nums1 1,2,3 <- pointer1  
        # one traverse pointer, start at the end of nums2  2,5,6 <- pointer2
        # if pointer 1 val > pointer 2 val, pointer 3 val = pointer1 val, move both pointer 1 and pointer 3
        # else same

        pw = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0: # both inbound
            if nums1[p1] > nums2[p2]:
                nums1[pw] = nums1[p1]
                pw -= 1
                p1 -= 1
            else:
                nums1[pw] = nums2[p2]
                pw -= 1
                p2 -= 1
        while p1 >= 0: # used all p2 , we can actually pass this because if we used all p2, p1 is already in place
            nums1[pw] = nums1[p1]
            pw -= 1
            p1 -= 1
        
        while p2 >= 0:
            nums1[pw] = nums2[p2]
            pw -= 1
            p2 -= 1