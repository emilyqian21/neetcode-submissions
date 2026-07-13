class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set) # c1: set(), c2: set()
        row = defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue 
                box_id = (r//3)*3 + c//3
                if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in box[box_id]:
                    return False
                else:
                    col[c].add(board[r][c])
                    row[r].add(board[r][c])
                    box[box_id].add(board[r][c])
        return True
