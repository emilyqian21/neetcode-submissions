class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isend = True
        

    def search(self, word: str) -> bool:
        
        def dfs(trienode, widx):
            # means from trienode can we find the word[widx:], return boolean. 
            if not trienode:
                return False
            if widx == len(word):
                return trienode.isend
           
            
            c = word[widx]
            if c == ".":
                for child in trienode.children.values():#all trienodes
                    if dfs(child, widx + 1):
                        return True
                return False

            elif c not in trienode.children:
                return False

            else:
                return dfs(trienode.children[c], widx + 1)
            
        
        return dfs(self.root, 0)


        
