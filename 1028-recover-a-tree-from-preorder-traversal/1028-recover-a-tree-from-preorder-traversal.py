# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preOrderTrav = ""
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.preOrderTrav = traversal
        def recursive(level):
            if self.preOrderTrav == "": return None
            
            # numberOfDashes = 0
            try:
                indexOfDash = self.preOrderTrav.index('-')
            except:
                indexOfDash = -1
            
            if indexOfDash == -1:
                root = TreeNode(int(self.preOrderTrav))
                return root
            
            try:
                indexOfDash = self.preOrderTrav.index('-')
            except:
                indexOfDash = -1
            root = TreeNode(int(self.preOrderTrav[0:indexOfDash]))
            self.preOrderTrav = self.preOrderTrav[indexOfDash:]
            numberOfDashes = 0
            for ch in self.preOrderTrav:
                if ch != '-':
                    break
                else:
                    numberOfDashes += 1
            if numberOfDashes > level:
                self.preOrderTrav = self.preOrderTrav[numberOfDashes:]
                root.left = recursive(level + 1)
                
            numberOfDashes = 0
            for ch in self.preOrderTrav:
                if ch != '-':
                    break
                else:
                    numberOfDashes += 1
            
            if numberOfDashes > level:
                self.preOrderTrav = self.preOrderTrav[numberOfDashes:]
                root.right = recursive(level + 1)
            
#             numberOfDashes = 0
#             for ch in preOrderTrav:
#                 if ch != '-':
#                     break
#                 else:
#                     numberOfDashes += 1
            
#             if numberOfDashes <= level:
#                 return root
            return root
        return recursive(0)
            
            