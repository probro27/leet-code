from typing import Optional

class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.linkedList = None
        self.endNode = None
        self.currentLength = 0
        self.elementNodeMap = {}

    def get(self, key: int) -> int:
        currentNode = self.linkedList
        if currentNode is None:
            return -1
        currentNode = self.elementNodeMap.get(key, None)
        if currentNode is None:
            return -1
        prevNode = currentNode.prev
        nextNode = currentNode.next
        if prevNode is None:
            return self.map.get(key, -1)
        if nextNode is None:
            self.endNode = prevNode
        else:
            nextNode.prev = prevNode
        prevNode.next = nextNode
        currentNode.next = self.linkedList
        if self.linkedList is not None:
            self.linkedList.prev = currentNode
        currentNode.prev = None
        self.linkedList = currentNode
        return self.map.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key] = value
            currentNode = self.elementNodeMap[key]
            prevNode = currentNode.prev
            nextNode = currentNode.next
            if prevNode is None:
                return
            if nextNode is None:
                self.endNode = prevNode
            else:
                nextNode.prev = prevNode
            prevNode.next = nextNode
            currentNode.next = self.linkedList
            if self.linkedList is not None:
                self.linkedList.prev = currentNode
            currentNode.prev = None
            self.linkedList = currentNode
        else:
            newNode = Node(key)
            self.map[key] = value
            self.elementNodeMap[key] = newNode
            newNode.next = self.linkedList
            if self.linkedList is not None:
                self.linkedList.prev = newNode
            else:
                self.endNode = newNode
            self.linkedList = newNode
            if self.currentLength == self.capacity:
                del self.map[self.endNode.key]
                del self.elementNodeMap[self.endNode.key]
                prevNode = self.endNode.prev
                prevNode.next = None
                self.endNode = prevNode
                return
            self.currentLength += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)