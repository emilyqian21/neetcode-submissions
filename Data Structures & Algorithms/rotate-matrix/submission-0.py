class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # step 1: transpose 
        # step 2: reflection 

        # time: O(n^2)
        # space: O(1)

        n = len(matrix)

        # 1. transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. reflection
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]