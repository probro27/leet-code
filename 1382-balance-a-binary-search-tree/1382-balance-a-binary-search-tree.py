# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def convertArrayToBST(self, lst: List[int]) -> TreeNode:
        if lst == []:
            return None
        
        mid = len(lst) // 2
        root = TreeNode(lst[mid])
        
        root.left = self.convertArrayToBST(lst[0:mid])
        root.right = self.convertArrayToBST(lst[mid + 1:])
        
        return root
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        
        def recursive(root, lst):
            if not root:
                return lst
            lst.append(root.val)
            
            lst = recursive(root.left, lst)
            lst = recursive(root.right, lst)
            
            return lst
        lst = recursive(root, lst)
        lst.sort()
        return self.convertArrayToBST(lst)
        