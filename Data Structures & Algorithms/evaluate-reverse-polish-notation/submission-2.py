class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use stack to append two numbers into stack
        # Then pop out two numbers and do operations
        # Then push the result back to stack
        # Question: how to convert string operators into actual operators?
        # Time: O(n), space: O(n)
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(c))
        
        return stack[0]