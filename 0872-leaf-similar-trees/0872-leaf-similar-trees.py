# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaves(self, root: Optional[TreeNode], leaves:List[int]) -> None:
        if root.left is None and root.right is None:
            leaves.append(root.val)
            return
        else:
            if root.left is not None:
                self.getLeaves(root.left, leaves)
            if root.right is not None:
                self.getLeaves(root.right, leaves)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        self.getLeaves(root1, leaves1)
        leaves2 = []
        self.getLeaves(root2, leaves2)
        return leaves1 == leaves2