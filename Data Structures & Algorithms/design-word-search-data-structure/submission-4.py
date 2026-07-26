class TrieNode:
    def __init__(self):
        self.children = {} # key = character, value = trienode
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] # move to next 
        # after the loop mark isEnd to true
        cur.isEnd = True
        

    def search(self, word: str) -> bool:

        def dfs(start, root):

            
            cur = root

            for i in range(start, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs( i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            # end of for statement, return True
            return cur.isEnd
        return dfs(0,self.root)
        
