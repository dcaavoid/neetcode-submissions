class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking with DFS, but forgot how to implement.
        # Count the number of current open and close parentheses.
        # if open == close == 0, all parentheses are well-formed and return;
        # if open > n, it's safe to add an open parenthesis;
        # if open > close, it's safe to add a close parenthesis.
        # Since string is non-mutable, use stack to perform backtracking.
        stack = []  # Track current valid parentheses strings
        res = []    # List of valid parenthese strings

        def backtrack(openP, closeP):
            # Base case:
            if openP == closeP == n:
                res.append("".join(stack))
                return
            
            # Recursive: add new parenthesis
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closeP)
                stack.pop()
            
            if openP > closeP: 
                stack.append(")")
                backtrack(openP, closeP + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res



