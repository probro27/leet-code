class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = '0'
        for digit in n:
            if digit > max_digit:
                max_digit = digit
        return ord(max_digit) - ord('0')
