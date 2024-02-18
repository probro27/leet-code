from collections import deque

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def printList(self):
        current = self
        while current is not None:
            print(str(current.val) + " -> " if current.next is not None else str(current.val), end="")
            current = current.next
        print("\n")

class LinkedList:
    head: ListNode
    def __init__(self):
        self.head = None

class Solution:
    def __init__(self):
        self.adj_list: List[LinkedList] = []
        self.colour: List[str] = []
        self.comp: List[int] = []

    def createGraph(self, grid: List[List[str]]):
        number_of_nodes = 0
        grid_to_number_map = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid_to_number_map[(i, j)] = number_of_nodes
                    number_of_nodes += 1
        print(grid_to_number_map)
        self.adj_list = [LinkedList() for _ in range(number_of_nodes)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    current_node = grid_to_number_map[(i, j)]
                    if i > 0 and grid[i - 1][j] == "1":
                        neighbour = grid_to_number_map[(i - 1, j)]
                        current = ListNode(neighbour)
                        current.next = self.adj_list[current_node].head
                        self.adj_list[current_node].head = current
                    if i < len(grid) - 1 and grid[i + 1][j] == "1":
                        neighbour = grid_to_number_map[(i + 1, j)]
                        current = ListNode(neighbour)
                        current.next = self.adj_list[current_node].head
                        self.adj_list[current_node].head = current
                    if j > 0 and grid[i][j - 1] == "1":
                        neighbour = grid_to_number_map[(i, j - 1)]
                        current = ListNode(neighbour)
                        current.next = self.adj_list[current_node].head
                        self.adj_list[current_node].head = current
                    if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
                        neighbour = grid_to_number_map[(i, j + 1)]
                        current = ListNode(neighbour)
                        current.next = self.adj_list[current_node].head
                        self.adj_list[current_node].head = current
                        
    def BFS(self, start: int, compNum: int):
        queue = deque([start])
        self.colour[start] = "grey"
        while len(queue) != 0:
            current_node = queue.popleft()
            current_nbr = self.adj_list[current_node].head
            self.comp[current_node] = compNum
            while current_nbr is not None:
                if self.colour[current_nbr.val] == "white":
                    queue.append(current_nbr.val)
                    self.colour[current_nbr.val] = "grey"
                current_nbr = current_nbr.next
            self.colour[current_node] = "black"


    def numIslands(self, grid: List[List[str]]) -> int:
        self.createGraph(grid)
        self.colour = ["white" for _ in self.adj_list]
        self.comp = [0 for _ in self.adj_list]
        compNum = 1
        for start in range(0, len(self.adj_list)):
            if self.colour[start] == "white":
                self.BFS(start, compNum)
                compNum += 1
        return (compNum - 1)