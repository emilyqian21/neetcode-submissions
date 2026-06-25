class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])
        visited = set()
        def dfs(r,c,i): # currently at position (r,c),already matched word [:i], trying to match word[i:]
            #when record an answer?
            if i == len(word):
                return True
            #pruning: no need to further explore if we reach this state
            if r >= nrows or c >= ncols or r < 0 or c < 0 or board[r][c] != word[i] or (r,c) in visited:
                return False
            
            #explore all possibilities
            #current node
            visited.add((r,c))
            #keep exploring from current path
            left = dfs(r-1,c,i+1)
            right = dfs(r+1,c,i+1)
            up = dfs(r,c+1,i+1)
            down = dfs(r,c-1,i+1)
            
        
            # cancel decision
            visited.remove((r,c))

            #return 
            return left or right or up or down
        
        for r in range(nrows):
            for c in range(ncols):
                if dfs(r,c,0): # whenver it reaches 'return', it will exit the whole for loop, the for loop wwill end
                    return True
        return False