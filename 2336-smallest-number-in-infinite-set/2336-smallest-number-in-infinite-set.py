class SmallestInfiniteSet:
    heap: List[int]
    removedElements: Set[int]

    def __init__(self):
        self.heap = []
        self.removedElements = set()
        for i in range(1, 1001):
            self.heap.append(i)
        self.heapify()

    def parent(self, i: int) -> Optional[int]:
        parentIndex= (i - 1) // 2
        if parentIndex >= 0 and parentIndex < len(self.heap):
            return parentIndex
        else:
            return None
    
    def last(self) -> int:
        return len(self.heap) - 1
    
    def leftChild(self, i) -> int:
        return (2 * i) + 1
    
    def rightChild(self, i) -> int:
        return self.leftChild(i) + 1

    def isLeaf(self, i: int) -> bool:
        leftChildIndex = self.leftChild(i)
        return leftChildIndex >= 0 and leftChildIndex < len(self.heap)

    def fixUp(self, i: int) -> None:
        while self.parent(i) is not None and self.heap[self.parent(i)] > self.heap[i]:
            temp = self.heap[i]
            self.heap[i] = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = temp
            i = self.parent(i)
    
    def fixDown(self, i: int) -> None:
        while self.isLeaf(i):
            j = self.leftChild(i)
            r = self.rightChild(i)
            if r >= 0 and r < len(self.heap) and self.heap[j] > self.heap[r]:
                j = r
            if self.heap[i] < self.heap[j]:
                break
            temp = self.heap[j]
            self.heap[j] = self.heap[i]
            self.heap[i] = temp
            i = j

    def heapify(self) -> None:
        for i in range(self.parent(self.last()), -1):
            self.fixDown(i)

    def popSmallest(self) -> int:
        temp = self.heap[0]
        self.heap[0] = self.heap[self.last()]
        self.heap.pop()
        self.fixDown(0)
        self.removedElements.add(temp)
        return temp

    def addBack(self, num: int) -> None:
        if num in self.removedElements:
            self.heap.append(num)
            self.fixUp(self.last())
            self.removedElements.remove(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)