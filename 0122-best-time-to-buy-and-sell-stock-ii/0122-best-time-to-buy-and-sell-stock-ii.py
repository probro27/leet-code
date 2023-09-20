class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        current_price = 0
        next_price = 1
        stock_owned = False
        stock_buying_price = 0
        max_profit = 0

        while next_price < len(prices):
            if stock_owned:
                if prices[current_price] > prices[next_price]:
                    max_profit += prices[current_price] - stock_buying_price
                    stock_owned = False
            else:
                if prices[current_price] < prices[next_price]:
                    stock_buying_price = prices[current_price]
                    stock_owned = True
            current_price += 1
            next_price += 1
        
        if stock_owned:
            if prices[current_price] > stock_buying_price:
                max_profit += prices[current_price] - stock_buying_price
        
        return max_profit


