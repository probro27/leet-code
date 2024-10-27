"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.distinctNodes = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        if node.val in self.distinctNodes:
            return self.distinctNodes[node.val]

        clone = Node(node.val)
        self.distinctNodes[node.val] = clone
        
        neighbors = []

        for neighbor in node.neighbors:
            neighbors.append(self.cloneGraph(neighbor))
        
        clone.neighbors = neighbors

        return clone
        