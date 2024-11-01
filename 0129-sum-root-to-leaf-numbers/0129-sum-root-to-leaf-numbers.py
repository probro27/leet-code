# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNum(root: Optional[TreeNode], currentNum: int) -> int:
            if root is None:
                return currentNum
            
            currentNum = (currentNum * 10) + root.val

            left_num = 0
            right_num = 0

            if root.left is not None:
                left_num = sumNum(root.left, currentNum)
            if root.right is not None:
                right_num = sumNum(root.right, currentNum)

            return (left_num + right_num) if left_num or right_num else currentNum
        
        return sumNum(root, 0)