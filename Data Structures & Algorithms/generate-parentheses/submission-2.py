class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtrack
        # Each step: choose "(" if # of "(" is less than n, or choose ")".
        # Good for add: open > close, and open < n.
        # Valid formation: open = close = n.
        res = []    # List of valid parentheses
        stack = []  # Current parentheses in DFS

        # Save all possible valid parentheses to res
        def dfs(openP: int, closeP: int):
            # Base case
            if n == openP and n == closeP:
                res.append("".join(stack))
                return
            
            # Recursive
            if openP < n:
                stack.append("(")
                dfs(openP + 1, closeP)
                stack.pop()
            if closeP < openP:
                stack.append(")")
                dfs(openP, closeP + 1)
                stack.pop()
            return

        dfs(0, 0)
        return res