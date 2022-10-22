# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    levels: [int] = []
    def createLevels(self, root: Optional[TreeNode], currentLevel: int):
        if root is None:
            return
        if len(self.levels) < currentLevel:
            self.levels.append([root.val])
        else:
            self.levels[currentLevel - 1].append(root.val)
        self.createLevels(root.left, currentLevel + 1)
        self.createLevels(root.right, currentLevel + 1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levels = []
        self.createLevels(root, 1)
        print(self.levels)
        result = []
        for row in self.levels:
            result.append(row[-1])
        return result