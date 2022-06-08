# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def numberOfNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return (1 + self.numberOfNodes(root.left) +  self.numberOfNodes(root.right))
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        leftHeight = self.numberOfNodes(root.left)
        
        if leftHeight + 1 == k:
            return root.val
        
        if leftHeight + 1 < k:
            return self.kthSmallest(root.right, k - leftHeight - 1)
        
        
        return self.kthSmallest(root.left, k)