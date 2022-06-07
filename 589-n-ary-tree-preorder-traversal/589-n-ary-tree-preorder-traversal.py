"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        lst = []
        
        def recursive(root, lst):
            if not root:
                return lst
            
            lst.append(root.val)
            if root.children:
                for child in root.children:
                    lst = recursive(child, lst)
            
            return lst
        return recursive(root, lst)