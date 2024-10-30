class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pathP = []
        self.pathQ = []
        
    def dfs(self, root: 'TreeNode', x: 'TreeNode', key: str) -> bool:
        if root is None:
            return False
    
        if root.val == x.val:
            if key == 'p':
                self.pathP.append(root)
            else:
                self.pathQ.append(root)
            return True
        
        left = self.dfs(root.left, x, key)
        right = self.dfs(root.right, x, key)
        
        if left or right:
            if key == 'p':
                self.pathP.append(root)
            else:
                self.pathQ.append(root)
            return True

        return False
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pFound = self.dfs(root, p, 'p')
        qFound = self.dfs(root, q, 'q')
        
        if not pFound or not qFound:
            return None
        
        pathP = self.pathP[::-1]
        pathQ = self.pathQ[::-1]
        
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i] != pathQ[i]:
                return pathP[i - 1]

        return None
