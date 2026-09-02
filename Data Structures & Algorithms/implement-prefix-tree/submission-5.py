class TrieNode:
    def __init__(self):
        self.children = {} # key = character, val = TrieNode()
        self.isend = False # is end of the word

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
             

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w] 
        cur.isend = True
        
    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w not in cur.children:
                return False
            else:
                cur = cur.children[w]
        
        return cur.isend
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for w in prefix:
            if w not in cur.children:
                return False
            else:
                cur = cur.children[w]
        return True
        