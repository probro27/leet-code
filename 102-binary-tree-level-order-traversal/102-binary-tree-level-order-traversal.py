# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
	    self.traversal = []

    def levelOrderAcc(self, root, level):
        if root:
            if len(self.traversal) == level:
                self.traversal.append([])
            self.traversal[level].append(root.val)
            self.levelOrderAcc(root.left, level + 1)
            self.levelOrderAcc(root.right, level + 1)
			
    def levelOrder(self, root):
        # we need an array
        # we need to know which level we are on
        self.levelOrderAcc(root, 0)
        return self.traversal