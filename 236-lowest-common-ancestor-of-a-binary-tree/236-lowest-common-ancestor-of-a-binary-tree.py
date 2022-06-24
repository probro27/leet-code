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
    
    def recursiveSearch(self, root: 'TreeNode', p: 'TreeNode') -> str:
        if not root:
            return "-1"
        if root == p:
            return "Found"
        else:
            leftStr = "0"  + self.recursiveSearch(root.left, p)
            rightStr = "1" + self.recursiveSearch(root.right, p)
            if leftStr[len(leftStr) - 2: len(leftStr)] != "-1":
                return leftStr
            else:
                return rightStr
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        resP = self.recursiveSearch(root, p)
        resQ = self.recursiveSearch(root, q)
        
        # print(f"{resQ} = resQ")
        
        commonStr = ""
        for i in range(min(len(resP), len(resQ))):
            if resP[i] == resQ[i]:
                commonStr += resP[i]
            else:
                break
                    
        # print(commonStr)
        # return root
        return self.nodeFollowingString(root, commonStr)