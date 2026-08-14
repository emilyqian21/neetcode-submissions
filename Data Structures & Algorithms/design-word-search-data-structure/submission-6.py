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
            # base case
            if i == len(word):
                return node.isEnd

            c = word[i]

            # Case 1: wildcard "."
            if c == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            # Case 2: normal character, but doesn't exist
            elif c not in node.children:
                return False

            # Case 3: normal character and exists
            else:
                return dfs(i + 1, node.children[c])
        return dfs(0, self.root)