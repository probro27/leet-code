class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def __init__(self):
        self.nodes = set()

    
    def lowestCommonAncestor(self, p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = p
        while current is not None:
            self.nodes.add(current)
            current = current.parent
            
        current = q
        while current is not None:
            if current in self.nodes:
                return current
            current = current.parent
        
        return None
