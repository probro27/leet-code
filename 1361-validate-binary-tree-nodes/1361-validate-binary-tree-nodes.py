class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parentMap = {i: -1 for i in range(n)}

        for i in range(n):
            left, right = leftChild[i], rightChild[i]

            if left != -1:
                if parentMap[left] != -1:
                    return False
                parentMap[left] = i
            
            if right != -1:
                if parentMap[right] != -1:
                    return False
                parentMap[right] = i
        
        count = 0
        for node, parent in parentMap.items():
            if parent == -1:
                count += 1
            
            current = parent
            path = set([node])
            while current != -1:
                if current in path:
                    return False
                path.add(current)
                current = parentMap[current]
        
        return count == 1
            