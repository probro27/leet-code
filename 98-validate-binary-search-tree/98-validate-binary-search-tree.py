# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(self, node, left, right):
            if not node:
                return True
            elif node.val <= left or node.val >= right:
                return False
            else:
                return (dfs(self, node.left, left, node.val) and dfs(self, node.right, node.val, right))
        return dfs(self, root, float("-inf"), float("inf"))