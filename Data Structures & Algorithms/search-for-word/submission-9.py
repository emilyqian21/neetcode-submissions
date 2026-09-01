class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow = len(board)
        ncol = len(board[0])
        visited = set()

        def dfs(r, c, path, widx):
            # return boolean, if there is word match from board[r][c] to match word[widx]. path is historical path, not include current node
            if widx == len(word): # find all characters
                return True
            if r < 0 or r >= nrow or c < 0 or c >= ncol or (r,c) in visited or board[r][c] != word[widx]:
                return False
           
            
            # choose. now inbound, and board[r][c] == word[widx]
            path.append(board[r][c])
            visited.add((r,c))
            # explore
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if dfs(nr, nc, path, widx + 1):
                    return True
            # undo
            path.pop()
            visited.remove((r,c))

          
        
        for r in range(nrow):
            for c in range(ncol):
                print(board[r][c])
                if board[r][c] == word[0]:
                    
                    if dfs(r, c, [], 0):
                        return True
        return False
