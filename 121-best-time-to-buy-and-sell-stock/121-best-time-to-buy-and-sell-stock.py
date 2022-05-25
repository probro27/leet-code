class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        if len(prices) == 1:
            return 0
        
        left = 0
        right = 1
        
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if currentProfit > maxProfit:
                maxProfit = currentProfit
            if prices[left] > prices[right]:
                left = right
            right = right + 1
        
        return maxProfit