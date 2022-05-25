class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterTable = {}
        
        if len(s) != len(t):
            # print(f"{les(s) and len(t)}")
            return False
        
        for i in s:
            if i in letterTable.keys():
                letterTable[i] += 1
            else:
                letterTable[i] = 1
        
        for j in t:
            if j not in letterTable.keys():
                return False
            elif letterTable[j] == 0:
                return False
            else:
                letterTable[j] -= 1
        
        return True
        