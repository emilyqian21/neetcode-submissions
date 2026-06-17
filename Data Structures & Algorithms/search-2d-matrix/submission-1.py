class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        nrow = len(matrix)
        ncol = len(matrix[0])

        l = 0
        r = nrow * ncol - 1

        while l <= r:
            mid = l + (r-l)//2 # (l+r)//2
            mid_r  = mid // ncol 
            mid_c = mid % ncol

            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] < target:
                l = mid + 1
            else:
                r = mid -1

        return False

        # time: O(log m*n)
        # spaceL O(1)