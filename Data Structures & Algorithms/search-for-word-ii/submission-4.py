class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Knew that I should turn words into Trie, but not sure how to find all words
        # Instead of checking each word at every possible starting coordinate, I can check if this starting coordinate can be any of the words' start.
        # Build Trie
        root = TrieNode()
        for word in words:
            root.add(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        # Given coordiante (r,c), current TrieNode and word built, search and save words in board into res.
        def backtrack(r, c, node, word):
            # Base case
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in visited or
                board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            # Backtrack
            backtrack(r + 1, c, node, word)
            backtrack(r - 1, c, node, word)
            backtrack(r, c + 1, node, word)
            backtrack(r, c - 1, node, word)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")
        
        return list(res)

