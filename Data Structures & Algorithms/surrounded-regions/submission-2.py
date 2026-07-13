class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Turn "capture all surrounded region" into "capture everything except unsurrounded region".
        # 1. Find all 0s on the border b/c it's always unsurrounded.
        # 2. Connect unsurounded region (DFS/BFS). (O -> T)
        # 3. Capture everything except unsurrounded region. (O -> X), then (T -> O)
        # Two version:
        # Version 1: DFS
        # ROWS, COLS = len(board), len(board[0])

        # # Connect all border land starting at (r, c)
        # def dfs(r, c):
        #     # Base case:
        #     if (r < 0 or r == ROWS or c < 0 or c == COLS or
        #         board[r][c] != "O"):
        #         return
            
        #     # Mark border land as T and recursively check four directions.
        #     board[r][c] = "T"
        #     dfs(r - 1, c)
        #     dfs(r + 1, c)
        #     dfs(r, c - 1)
        #     dfs(r, c + 1)

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         # If it's land and it's a border land.
        #         if (board[r][c] == "O" and
        #             (r in [0, ROWS - 1] or
        #              c in [0, COLS - 1])):
        #             dfs(r, c)
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c] == "O":
        #             board[r][c] = "X"
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if board[r][c] == "T":
        #             board[r][c] = "O"
        

        # ------------------------------------------------------------------------------------
        # Version 2: BFS
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            q = collections.deque([(r, c)])

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and
                        board[r][c] == "O"):
                        board[r][c] = "T"
                        q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1)):
                    board[r][c] = "T"
                    bfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
