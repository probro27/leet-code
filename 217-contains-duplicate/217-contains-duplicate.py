class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        indexMap = {}
        
        for i in nums:
            indexMap[i] = 0
        
        for j in nums:
            indexMap[j] += 1
            if indexMap[j] > 1:
                return True
        
        return False