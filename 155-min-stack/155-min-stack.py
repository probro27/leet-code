class MinStack:
    
    stack: [int]
    # stackLen: int
    minElement: int
    
    def __init__(self):
        self.stack = []
        # self.stackLen = 0
        self.minElement = sys.maxsize
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minElement:
            self.minElement = val
        # self.stackLen

    def pop(self) -> None:
        res = self.stack.pop()
        if res == self.minElement:
            if self.stack != []:
                self.minElement = min(self.stack)
            else:
                self.minElement = sys.maxsize

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()