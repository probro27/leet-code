# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return (1 + max(self.heightBinaryTree(root.left), self.heightBinaryTree(root.right)))
    
    def findMaxHeightSum(self, root: Optional[TreeNode], maxSum: int) -> int:
        if not root:
            return maxSum
        sumOfBranchHeights = self.heightBinaryTree(root.left) + self.heightBinaryTree(root.right) 
        if sumOfBranchHeights > maxSum:
            maxSum = sumOfBranchHeights
        return max(self.findMaxHeightSum(root.left, maxSum), self.findMaxHeightSum(root.right, maxSum))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.findMaxHeightSum(root, 0)