class TrieNode:
    def __init__(self):
        self.children = {}    # Hash map that character: TrieNode.
        self.isWord = False   # If the current TrieNode is a end of word.

    # Add new word to Trie
    def addWord(self, word: str):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
    
    # o a a n
    # e t a e
    # i h k r
    # i f l v

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the list of words into a Trie for easier characters retrieval.
        # Then for each letter on board, check if it's a valid starting character,
        # if yes, can use either BFS/DFS to start searching.
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        visited = set()    # (r, c): visited coordinate in board in current BFS/DFS.
        res = set()           # list of result words.

        # DFS: starting at board[r][c] and current node in Trie, build word
        def dfs(r, c, node, word):
            # Base case
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in visited or board[r][c] not in node.children):
                return
            
            # Add current character and check if current word is valid.
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isWord:
                res.add(word)

            # Recursive: check surrounding boards
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visited.remove((r, c))
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root, "")
        
        return list(res)


        