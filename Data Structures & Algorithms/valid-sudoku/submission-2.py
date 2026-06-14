class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                #traverse each unit in the board
                if board[r][c] == ".":
                    continue
                if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in box[(r//3,c//3)]:
                    return False
                else:
                    # add it into the seen sets
                    col[c].add(board[r][c])
                    row[r].add(board[r][c])
                    box[(r//3, c//3)].add(board[r][c])

        return True 