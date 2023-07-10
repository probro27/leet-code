# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxValueNode(self, root: TreeNode, maxVal: int) -> int:
        if root is not None:
            if root.val >= maxVal:
                return 1 + self.maxValueNode(root.left, root.val) + self.maxValueNode(root.right, root.val)
            else:
                return self.maxValueNode(root.left, maxVal) + self.maxValueNode(root.right, maxVal)
        else:
            return 0

    def goodNodes(self, root: TreeNode) -> int:
        return self.maxValueNode(root, root.val)