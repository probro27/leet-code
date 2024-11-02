# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        start = root
        queue = deque([(start, 0, 0)])

        position = 1

        while len(queue) != 0:
            currentNode, currentLevel, currentColumn = queue.popleft()

            if position != (2 ** currentLevel + currentColumn):
                return False
            
            if currentNode.left:
                queue.append((currentNode.left, currentLevel + 1, currentColumn * 2))
            if currentNode.right:
                queue.append((currentNode.right, currentLevel + 1, currentColumn * 2 + 1))

            position += 1

        return True
