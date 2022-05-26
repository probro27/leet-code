class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        indexMap = {}
        
        for i in nums:
            indexMap[i] = 0
        
        for j in nums:
            indexMap[j] += 1
        maxCount = 0
        maxElement = 0
        for k in indexMap.keys():
            if maxCount < indexMap[k]:
                maxCount = indexMap[k]
                maxElement = k
        
        return maxElement