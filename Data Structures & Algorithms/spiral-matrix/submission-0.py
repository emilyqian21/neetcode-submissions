class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(m * n)
        # Space: O(1) extra space
        #
        # Keep 4 boundaries of the remaining unvisited rectangle.
        # Traverse: top -> right -> bottom -> left.
        # After finishing one side, move that boundary inward.

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = []

        while top <= bottom and left <= right:

            # 1. top row: left -> right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. right column: top -> bottom
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3. bottom row: right -> left
            # Check because top may have crossed bottom.
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4. left column: bottom -> top
            # Check because left may have crossed right.
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res