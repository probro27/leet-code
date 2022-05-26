# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 1
        high = n
        
        while low != high:
            mid = (high + low) // 2
            res = isBadVersion(mid)
            
            if res == True:
                high = mid
            else:
                low = mid + 1
                
        return low