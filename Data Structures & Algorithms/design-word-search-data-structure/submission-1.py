class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.isEnd = True
        
    
    # DFS with backtracking to search every possible path for "."
    def search(self, word: str) -> bool:
        def dfs(index, node):
            cur = node

            for i in range(index, len(word)):
                c = word[i]

                # If dot: search all possible values in the hash map with backtracking
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    
                    return False
                # Regular lowercase character
                else:
                    if c not in cur.children:
                        return False
                    
                    cur = cur.children[c]
            
            return cur.isEnd
        
        return dfs(0, self.root)
