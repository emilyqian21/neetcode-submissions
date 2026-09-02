class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colvisited = set() # unique c
        posvisited = set() # unique (r + c)
        negvisited = set() # unique (r - c)
        board = [["."] * n  for _ in range(n)] # [[".", ".",".","."],[".", ".",".","."]]
        
        res = []
        def dfs(r):
            # traverse all possibility to put Q in row r
            if r == n:
                copy = ["".join(r) for r in board]
              
                res.append(copy)
                return 
 
            # choose
            for c in range(n):
                if c in colvisited or (r + c) in posvisited or (r - c) in negvisited:
                    continue

                colvisited.add(c)
                posvisited.add((r + c))
                negvisited.add((r - c))
                board[r][c] = "Q"

                # explore
                dfs(r + 1)

                # undo
                colvisited.remove(c)
                posvisited.remove((r + c))
                negvisited.remove((r - c))
                board[r][c] = "."
            return
        dfs(0)
        return res


                 