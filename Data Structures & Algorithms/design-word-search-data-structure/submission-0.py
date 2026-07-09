class TrieNode:
    def __init__(self):
        self.children = {}
        self.endnode = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
                curr = curr.children[c]
            else:
                curr = curr.children[c]
        #end of word
        curr.endnode = True
        
    def search(self, word: str) -> bool:
  
        def helper(i,curr):
            for j in range(i,len(word)):
                if word[j] == ".":
                    for child in curr.children.values():
                        if helper(j+1,child):
                            return True
                    return False

                else: # word[i] !="."
                    if word[j] in curr.children:
                        curr = curr.children[word[j]]
                    else:
                        return False
            return curr.endnode 
        return helper(0,self.root)



