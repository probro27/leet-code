class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterTable = {}
        
        for i in s:
            letterTable[i] = 0
        
        for j in s:
            letterTable[j] += 1
        
        maxLenPalindrome = 0
        
        for i in s:
            res = letterTable[i]
            if res > 1:
                lenToAdd = res // 2
                maxLenPalindrome += (lenToAdd * 2)
                letterTable[i] -= (lenToAdd * 2)
        
        for j in letterTable.keys():
            if letterTable[j] == 1:
                maxLenPalindrome += 1
                break
        
        return maxLenPalindrome
            