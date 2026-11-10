class MinStack:

    def __init__(self):
        self.stack = []
        self.extraStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        newVal = min(val, self.extraStack[-1] if self.extraStack else val)
        self.extraStack.append(newVal)

    def pop(self) -> None:
        self.stack.pop()
        self.extraStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extraStack[-1]
        
