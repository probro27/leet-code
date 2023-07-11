# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    levels: List[int]

    def __init__(self):
        self.levels = []

    def maxLevelSumRecursive(self, root: Optional[TreeNode], level: int) -> None:
        if root is not None:
            if level >= len(self.levels):
                self.levels.append(root.val)
            else:
                self.levels[level] += root.val
            self.maxLevelSumRecursive(root.left, level + 1)
            self.maxLevelSumRecursive(root.right, level + 1)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.maxLevelSumRecursive(root, 0)
        print(self.levels)
        return (self.levels.index(max(self.levels)) + 1)