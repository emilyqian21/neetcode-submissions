class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find exact target
        nrow = len(matrix)
        ncol = len(matrix[0])
        size = nrow * ncol
        #edge case
        if not matrix:
            return False

        l = 0
        r = size - 1

        while l <= r:
            m = (l + r) // 2
            row_cord = m // ncol
            col_cord = m % ncol 
            cur_num = matrix[row_cord][col_cord]
            if cur_num == target:
                return True
            elif cur_num < target:
                l += 1
            else:
                r -= 1

        return False