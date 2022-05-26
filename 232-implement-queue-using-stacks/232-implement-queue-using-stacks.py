class MyQueue:
    
    stack1 : [int]
    stack2 : [int]
    
    def __init__(self):
        self.stack1 = []    
        self.stack2 = []

    def push(self, x: int) -> None:
        if self.stack2 == []:
            self.stack2.append(x)
        else:
            self.stack1.append(x)
            
    def pop(self) -> int:
        res = self.stack2.pop(0)
        if self.stack1 != []:
            newRes = self.stack1[0]
            self.stack1 = self.stack1[1:]
            self.stack2.append(newRes)
        return res

    def peek(self) -> int:
        return self.stack2[0]

    def empty(self) -> bool:
        if self.stack1 == [] and self.stack2 == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()