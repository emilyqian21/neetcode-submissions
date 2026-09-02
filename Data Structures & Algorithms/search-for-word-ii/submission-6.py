class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

    def insert(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isend = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        visited = set()
        nrow = len(board)
        ncol = len(board[0])

        self.root = TrieNode()
        for word in words:
            self.root.insert(word)


        def dfs(r, c, node, path):
            #traverse style. from baord[r][j],traverse node to see if there is a match to the end of the node. historical path saved in path, not include current node.
            if r < 0 or r >= nrow or c < 0 or c >= ncol or (r, c) in visited or  board[r][c] not in node.children:
                return 

            # choose 
            # board[r][c] in node.children
            visited.add((r, c))
            path.append(board[r][c])
            node = node.children[board[r][c]]
            
            if node.isend == True:
                res.append(''.join(path))
                # label the node.isend to False, so no need to traverse again
                node.isend = False

            # explore
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(nr, nc, node, path)
            # undo
            visited.remove((r, c))
            path.pop()

            return
        
        for r in range(nrow):
            for c in range(ncol):
                dfs(r, c, self.root, [])
        return res

                
            
