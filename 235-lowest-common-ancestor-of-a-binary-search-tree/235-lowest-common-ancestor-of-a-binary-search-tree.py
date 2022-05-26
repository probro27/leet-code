# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def nodeFollowingString(self, root: 'TreeNode', res: str) -> 'TreeNode':
        if res == "":
            return root
        elif res[0] == '0':
            return self.nodeFollowingString(root.left, res[1:])
        else:
            return self.nodeFollowingString(root.right, res[1:])
    
    def searchElement(self, root: 'TreeNode', p: 'TreeNode', res: str) -> str:
        if p.val < root.val:
            return self.searchElement(root.left, p, res + "0")
        elif p.val > root.val:
            return self.searchElement(root.right, p, res + "1")
        else:
            return res
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        resP = self.searchElement(root, p, "")
        resQ = self.searchElement(root, q, "")
        
        commonStr = ""
        for i in range(min(len(resP), len(resQ))):
            if resP[i] == resQ[i]:
                commonStr += resP[i]
            else:
                break
                    
                    
        return self.nodeFollowingString(root, commonStr)