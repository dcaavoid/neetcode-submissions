class MinStack:

    def __init__(self):
        # Two stacks: actual stack and min stack
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Push val to actual stack
        # Then push min val to min stack after comparison
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        
