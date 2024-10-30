from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonZeroMap = {index: num for index, num in enumerate(nums) if num != 0}
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        nonZeroMap = {}
        if len(self.nonZeroMap) <= len(vec.nonZeroMap):
            nonZeroMap = self.nonZeroMap
        else:
            nonZeroMap = vec.nonZeroMap
            
        for index in nonZeroMap.keys():
            if index in nonZeroMap:
                result += self.nonZeroMap[index] * vec.nonZeroMap[index]
        
        return result

    def dotProductAlt(self, vec: List[int]) -> int:
        return sum([vec[index] * value for index, value in self.nonZeroMap.items()])
