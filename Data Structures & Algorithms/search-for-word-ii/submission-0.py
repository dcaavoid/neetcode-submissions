# Use backtracking (DFS) on the borad to search for all possible words.
# For easier tracking of word, turn the list of words into a Trie.
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create a root node to build the list of words into a Trie.
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()     # Store words that are present in the board.
        visited = set()     # Store coordinates in board that are visited in the current backtracking.
        
        # Try all possible words starting at board[r, c] through backtracking (DFS).
        # node: node in the Trie; word: word that is built so far in the current backtracking.
        def dfs(row, col, node, word):
            # Base case: (1) out of bound; (2) current coordiate is visited; (3) current letter doesn't exist in the current Trie.
            if (row < 0 or col < 0 or
                row == ROWS or col == COLS or
                (row, col) in visited or board[row][col] not in node.children):
                return
            
            # Recursive
            visited.add((row, col))

            # Check if the current word from board exist in the list of words
            word += board[row][col]
            node = node.children[board[row][col]]
            if node.isEnd:
                res.add(word)
            
            # Check four directions
            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            # Remove the current coordinate once finished searching in the current backtracking.
            visited.remove((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
