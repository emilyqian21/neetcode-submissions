class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = nums1, nums2
        m, n = len(A), len(B)

        # Number of elements that should be on the left
        left_size = (m + n + 1) // 2 
        # 为什么是 (m + n + 1)而不是(m + n)? 当总元素数量是奇数时，让 left side 比 right side 多一个元素。

        l, r = 0, m
        # l = 当前最少考虑从 A 取多少个元素放到 left side
        # r = 当前最多考虑从 A 取多少个元素放到 left side

        while l <= r:
            # Number of elements taken from A
            i = (l + r) // 2

            # Number of elements taken from B
            j = left_size - i

            Aleft = A[i - 1] if i > 0 else float("-inf") # A[: i]有i个元素-->last element = A[i - 1]
            Aright = A[i] if i < m else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)

                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            # Took too many elements from A
            elif Aleft > Bright:
                r = i - 1

            # Took too few elements from A
            else:
                l = i + 1