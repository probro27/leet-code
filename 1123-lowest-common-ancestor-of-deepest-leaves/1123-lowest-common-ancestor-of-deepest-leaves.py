# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postOrder(node: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
            if not node:
                return (None, 0)
            
            left_lca, left_depth = postOrder(node.left)
            right_lca, right_depth = postOrder(node.right)

            if left_depth > right_depth:
                return (left_lca, left_depth + 1)
            elif left_depth < right_depth:
                return (right_lca, right_depth + 1)
            else:
                return (node, left_depth + 1)
        
        ret, _ = postOrder(root)

        return ret