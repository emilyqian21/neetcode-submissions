class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        #initilize the prefix tree with the root
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c] # move to the node of character c 
            else:
                # insert the node
                cur.children[c] = TrieNode()
                cur = cur.children[c]
        # after insertion, change is end to true
        cur.isEnd = True
        return

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c] # move to the node of character c
        # after the loop check if this is the end of tree
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True
        
        