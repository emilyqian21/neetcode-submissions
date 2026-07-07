class TrieNode:
    def __init__(self):
        self.children = {} # 'a':node(), 'b':node()
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
        #end of insert
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        