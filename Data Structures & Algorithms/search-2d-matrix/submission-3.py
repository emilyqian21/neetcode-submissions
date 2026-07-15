class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow = len(matrix)
        ncol = len(matrix[0])
        l = 0 
        r = nrow * ncol - 1

        while l <= r:
            m = (l + r)//2
            m_r = m//ncol
            m_c = m % ncol

            if matrix[m_r][m_c] == target:
                return True
            elif matrix[m_r][m_c] < target:
                l = m+ 1
            else:
                r = m- 1
        return False