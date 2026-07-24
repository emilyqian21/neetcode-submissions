class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        pos_diag_set = set() # r + c
        neg_diag_set = set() # r - c
        
        board = [ ["."]* n  for _ in range(n)]
        res = []
        def dfs(r): 
            # when to record answer
            if r == n: # already scanned the last row in the board
                res.append( ["".join(row) for row in board])
                return
            
            # make the choice
            for c in range(n):
                # only choose the position if valid
                if c in col_set or (r + c) in pos_diag_set or (r - c) in neg_diag_set:
                    continue
                
                # valid, made the choice
                board[r][c] = "Q"
                # update the sets
                col_set.add(c)
                pos_diag_set.add( r + c)
                neg_diag_set.add( r - c)

                #explore 
                dfs(r + 1)

                # undo
                board[r][c] = "."
                # update the sets
                col_set.remove(c)
                pos_diag_set.remove( r + c)
                neg_diag_set.remove( r - c)
        dfs(0)
        return res
