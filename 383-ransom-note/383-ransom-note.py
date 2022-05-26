class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        indexTable = {}
        
        for i in ransomNote:
            indexTable[i] = 0
        
        for i in ransomNote:
            indexTable[i] += 1
            
        for j in magazine:
            if j in indexTable.keys():
                if indexTable[j] != 0:
                    indexTable[j] -= 1
            
        for k in indexTable.keys():
            if indexTable[k] != 0:
                return False
        
        return True