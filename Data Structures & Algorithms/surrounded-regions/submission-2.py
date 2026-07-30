class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        nrow = len(board)
        ncol = len(board[0])

        def dfs(r,c):
            if (r < 0 or r >= nrow or c < 0 or c >= ncol or (r,c) in visited
            or board[r][c] != "O"):
                return
            #process current cell
            visited.add((r,c))

            for nr, nc in [(r + 1, c),(r - 1, c),(r, c + 1),(r, c - 1)]:
                dfs(nr,nc)
            return

        for c in range(ncol):
            dfs(0,c) 
            dfs(nrow -1, c)
        for r in range(nrow):
            dfs(r, 0)
            dfs(r, ncol - 1)
        
        for r in range(nrow):
            for c in range(ncol):
                if (r,c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"
        
                    
