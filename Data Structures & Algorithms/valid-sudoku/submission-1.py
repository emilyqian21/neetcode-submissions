class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) #set查找比list快
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row//3, col//3)]):
                    return False
                
                #if valid then add 
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row//3,col//3)].add(board[row][col]) #set 用add, list用append

        return True
        #time: O(n^2) for n*n grid
        #space: O(n^2) for n*n grid, because we can save n*n numbers at maximum