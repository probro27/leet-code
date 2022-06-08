class Solution:
    
    
    
    ## lst = [1,2], target = n = 3
    def howSum(self, lst: List[int], n: int) -> int:
        memo = {}
        def recursive(lst, n):
            if n in memo.keys(): return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0

            totalWays = 0

            for element in lst:
                remainder = n - element
                ways = recursive(lst, remainder)
                totalWays += ways
            
            memo[n] = totalWays
            return totalWays
        return recursive(lst, n)
    
    def climbStairs(self, n: int) -> int:
        return self.howSum([1,2], n)