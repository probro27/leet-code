class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def tribonacciHelper(n: int, memo: dict()) -> int:
            if n in memo.keys(): return memo[n]
            if n == 0: return 0
            if n <= 2:
                return 1
            memo[n] = tribonacciHelper(n - 1, memo) + tribonacciHelper(n - 2, memo) + tribonacciHelper(n - 3, memo)
            return memo[n]
        return tribonacciHelper(n, memo)