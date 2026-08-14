class TrieNode:
    def __init__(self):
        self.children = {} # key = character, value = trienode
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root # represent the TrieNode

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] # move to next 
        # after the loop mark isEnd to true
        cur.isEnd = True
        

    def search(self, word: str) -> bool:

        def dfs(i, node):
            # explicit base case
            if i == len(word):
                return node.isEnd

            c = word[i]

            if c == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            if c not in node.children:
                return False

            return dfs(i + 1, node.children[c])
        return dfs(0, self.root)