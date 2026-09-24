class TrieNode:

    def __init__(self):
        self.children = {}  # character -> TrieNode
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        
        # Search through backtracking
        # idx: inclusive index of start of searching word
        # node: current TrieNode in self.root
        def dfs(idx, node) -> bool:
            curr = node

            for i in range(idx, len(word)):
                # If this is a ".", search through backtracking
                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                # Or if this is an actual character
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            
            return curr.endOfWord
        
        return dfs(0, self.root)
            
            
