class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Space optimized: only push when val <= minStack[-1]
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        # Space optimized: only pop the min if val == minStack[-1]
        if self.minStack and val == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
