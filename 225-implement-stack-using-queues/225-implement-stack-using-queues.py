class MyStack:
        
    queue1: [int]
    queue2: [int]
    q1Len: int
    
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.q1Len = 0
        

    def push(self, x: int) -> None:
        if self.queue2 == []:
            self.queue2.append(x)
        else:
            res = self.queue2[0]
            if len(self.queue1) > self.q1Len:
                self.queue1[self.q1Len] = res
            else:
                self.queue1.append(res)
            self.q1Len += 1
            self.queue2[0] = x

    def pop(self) -> int:
        res = self.queue2.pop(0)
        if self.q1Len > 0:
            newRes = self.queue1[self.q1Len - 1]
            self.q1Len -= 1
            self.queue2.append(newRes)
        return res

    def top(self) -> int:
        return self.queue2[0]

    def empty(self) -> bool:
        if self.queue2 == [] and self.q1Len == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()