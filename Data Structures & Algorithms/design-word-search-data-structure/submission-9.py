class TrieNode:
    def __init__(self):
        self.children = {} # c : TrieNode()
        self.endword = False # if an word ends here


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] # move to next node
        cur.endword = True
        

    def search(self, word: str) -> bool: # return if word in self.root
        def dfs(cur, word):

            for i in range(len(word)):
                # .
                if word[i] == ".":
                    # make choice
                    for child in cur.children:
                        if dfs(cur.children[child], word[i + 1:]):
                            return True
                    return False # 必须要return 不然就会截止进入 for i in range(len(word))
                # not .
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            # end of for loop
            return cur.endword 
        return dfs(self.root, word)
            
