class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(coins, amount, memo):
            if amount in memo.keys(): return memo[amount]
            if amount == 0: return 0
            if amount < 0: return -1

            shortestChange = -1

            for coin in coins:
                remainder = amount - coin

                regCombination = helper(coins, remainder, memo)
                # print(f"remainder: {remainder}, regCombination: {regCombination}")
                if regCombination != -1:
                    combination = regCombination + 1

                    if shortestChange == -1 or combination < shortestChange:
                        shortestChange = combination

            memo[amount] = shortestChange
            return shortestChange
        return helper(coins, amount, memo)