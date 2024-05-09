# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSum(self, root: TreeNode, parentEven: bool) -> int:
        if root is None:
            return 0
        currentSum = 0
        if parentEven:
            if root.left is not None:
                currentSum += root.left.val
            if root.right is not None:
                currentSum += root.right.val
        currentEven = False
        if root.val % 2 == 0:
            currentEven = True
        
        left_sum = self.findSum(root.left, currentEven)
        right_sum = self.findSum(root.right, currentEven)

        return currentSum + left_sum + right_sum 
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.findSum(root, False)