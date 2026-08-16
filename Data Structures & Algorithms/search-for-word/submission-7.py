class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        nrow = len(board)
        ncol = len(board[0])
        visited = set()

        def dfs(r,c, widx):
            # return boolean. dfs(r,c, widx) means from board[r][c] if there is a match of word[widx:]
            # base case
            if widx == len(word):
                return True

            if r < 0 or r >= nrow or c < 0 or c >= ncol or (r,c) in visited or board[r][c] != word[widx]:
                return False
             
            
            # main logic
            # process cur cell, cur cell == word[widx]
            # make choice
            visited.add((r,c))

            # explore 4 directions recurisvely
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if dfs(nr, nc, widx + 1): # if from board[nr][nc] there is a match of word[widx + 1:], then this is true.
                    return True

            # undo the choice if it's not the right way
            visited.remove((r,c)) 
            
            return False # otherwise it's false 

        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False

