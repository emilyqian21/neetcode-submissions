class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrow = len(board)
        ncol = len(board[0])
        visited = set()

        def dfs(r,c,word_idx):
            # base case 1
            if ( r >= nrow or r < 0 or  c >= ncol
                or c< 0 or board[r][c] != word[word_idx]):
                return

            # base case 2
            if word_idx == len(word) - 1:
                return True

            # process current cell
            visited.add((r,c))
            # current cell is now guarenteed to be same as word[word_idx]
            # explore four directions
            for new_r, new_c in [(r + 1, c),(r - 1, c),(r, c + 1),(r, c - 1)]:
                # visited check
                if (new_r,new_c) in visited:
                    continue
                if dfs(new_r,new_c, word_idx + 1): 
                    return True # propogate the info upwards
                    
            # dfs(r + 1, c, word_idx + 1)
            # dfs(r - 1, c, word_idx + 1)
            # dfs(r, c + 1, word_idx + 1)
            # dfs(r, c - 1, word_idx + 1)

            # undo: word_idx is a parameter in the function, so no need to update
            visited.remove((r,c))

        
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == word[0]: 
                    if dfs(r,c,0):
                        return True
        return False

