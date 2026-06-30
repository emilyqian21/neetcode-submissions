class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #
        # 1. dfs on borader, turn "O" --> T
        # 2. for loop, change remaining "O" --> "X"
        # 3. for loop, change "T" --> "O"
        nrow = len(board)
        ncol = len(board[0])
        def dfs(r,c):
            # base case: when to stop searching and return
            if r >= nrow or r < 0 or c >= ncol or c < 0 or board[r][c] !="O":
                return
            board[r][c] = "T"
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_r, new_c = dr + r, dc + c
                dfs(new_r, new_c)
            return 
        
        #1. dfs on borader, turn "O" --> T
        for c in range(ncol):
            dfs(0,c)
            dfs(nrow - 1, c)
        
        for r in range(nrow):
            dfs(r,0)
            dfs(r, ncol - 1)

        # 2. for loop , change remaining "O" --> "X"
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # 3. for loop, change "T" --> "O"
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == "T":
                    board[i][j] = "O"