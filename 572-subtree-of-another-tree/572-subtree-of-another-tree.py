# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if((not p) and (not q)):
            return True
        elif ((not p) or (not q)):
            return False
        elif p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        elif root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True 
            else:
                return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        