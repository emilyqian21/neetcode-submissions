class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordend = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        nrows = len(board)
        ncols = len(board[0])
        visited = set()
        root = TrieNode()

        def add_words(w): 
            # no need to return; add word into trienode, modify in place
            curr = root # 易错点：应该每个word 都重新在root开始
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.wordend = True #易错点：每个word加完要update一下这个node的wordend属性

        def dfs(r, c, node, path):
            # no return value； dfs(r, c, node, path) means 从 board[r][c] 开始，在当前 Trie node 下继续匹配，把所有找到的 word 加进 res
            if r < 0 or r >= nrows or c < 0 or c >= ncols or (r,c) in visited or board[r][c] not in node.children:
                return 
            
            # main logic
            # now board[r][c] is in node.children
            # make choice
            char = board[r][c]
            path.append(char)
            visited.add((r,c))
            
            if node.children[char].wordend == True:
                res.add("".join(path))

            # explore four directions recursively
            for nr, nc in [(r + 1, c), ( r - 1, c), (r, c + 1), (r , c - 1)]:
                dfs(nr, nc, node.children[char], path)

            # undo
            path.pop()
            visited.remove((r,c))
            return 
        
        for w in words:
            add_words(w)
        
        for r in range(nrows):
            for c in range(ncols):
                dfs(r, c, root, [])

        return list(res)
            

