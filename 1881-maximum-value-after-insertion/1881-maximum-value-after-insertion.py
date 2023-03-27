class Solution:
    def maxValue(self, n: str, x: int) -> str:
        isNegative = n[0] == '-'
        m = n
        if isNegative:
            m = m[1:]
        result = ""
        for index, letter in enumerate(m):
            if isNegative:
                if x < int(letter):
                    first_half = m[0:index]
                    second_half = m[index:]
                    result = first_half + str(x) + second_half
                    break
            else:
                if x > int(letter):
                    first_half = m[0:index]
                    second_half = m[index:]
                    result = first_half + str(x) + second_half
                    break
        if result == "":
            result = m + str(x)
        if isNegative:
            result = '-' + result
        return result