# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        lst = []
        
        def recursive(root, lst):
            if not root:
                return lst
            
            lst.append(root.val)
            lst = recursive(root.left, lst)
            lst = recursive(root.right, lst)
            
            return lst
        return recursive(root, lst)