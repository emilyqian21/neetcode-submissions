class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        nrow = len(board)
        ncol = len(board[0])

        def dfs(r, c, widx): 
            # return boolean, if the word[idx:] exist in the board starting at r,c
            # base case
            if widx == len(word): # successfully matched every c in word
                return True
            if r < 0 or r >= nrow or c < 0 or c >= ncol or (r,c) in visited or board[r][c] != word[widx]:
                return False
          

            # main logic
            # make choice
            visited.add((r,c))

            # explore recursively
            for nr,nc in [(r + 1, c),(r - 1, c),(r, c + 1),(r, c - 1)]:
                if (nr,nc) in visited:
                    continue
                if dfs(nr, nc, widx + 1):
                    return True

            # undo
            visited.remove((r,c))
            return 
        
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False

        
