# Build Trie
class TrieNode:
    def __init__(self):
        self.children = {}  # character -> TrieNode
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        
        # Return 
        def dfs(i, node):
            curr = node

            for i in range(i, len(word)):
                c = word[i]

                # Two conditions:
                # 1. word[i] is a dot: search all possible TrieNode in curr.children.
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    
                    return False

                # 2. word[i] is a valid character:
                else:
                    if c not in curr.children:
                        return False
                    
                    curr = curr.children[c]
            
            return curr.isEnd
        
        return dfs(0, self.root)


        
