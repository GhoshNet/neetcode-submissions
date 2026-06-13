class MinStack:
    #We will be using one corresponding stack to maintain the min val
    def __init__(self):
        self.stack = []
        self.minStack =[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) #Add min Value or first value if it's there's no value yet(initial push)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
