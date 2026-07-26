class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def add_word(self,root, word):
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # end of for loop
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #1. add words to Trie 
        root = TrieNode()
        for word in words:
            root.add_word(root,word)
            # or self.add_word(root,word)?
        
        # 2. dfs
        nrow = len(board)
        ncol = len(board[0])
        visited = set()
        res = set()

        def dfs(r,c,word,node): # node is trienode
            # base case
            if r >= nrow or r < 0 or c >= ncol or c < 0 or (r,c) in visited or board[r][c] not in node.children:
                return
            
            # process current cell
            visited.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]] # 易错点， 在这行之前，node是上一级的，因为我们从root出发

            if node.isEnd == True: # at the end of one word
                res.add(word) # 易错点：这个之后不能return，因为我们要继续寻找其他词；比如 app结束了，我们要找apple

            # continue current path 
            for n_r, n_c in [(r + 1, c), (r - 1, c),(r, c + 1),(r, c - 1)]:
                dfs(n_r, n_c, word, node) # next child

            # backtrack undo
            visited.remove((r,c))

        for r in range(nrow):
            for c in range(ncol):
                dfs(r,c,"",root)
        return list(res)