class Solution:
    def __init__(self):
        self.charToOpMap = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
        }
        
    def evaluateOp(self, arithmetic_set, opCheck1, opCheck2) -> list:
        index_removal = set()
        for index, (num, op) in enumerate(arithmetic_set):
            if op == opCheck1 or op == opCheck2:
                next_num, next_op = arithmetic_set[index + 1]
                arithmetic_set[index + 1] = (self.charToOpMap[op](num, next_num), next_op)
                index_removal.add(index)
        
        new_arithmetic_set = []
        for index, (num, op) in enumerate(arithmetic_set):
            if index not in index_removal:
                new_arithmetic_set.append((num, op))
        
        return new_arithmetic_set

    def calculate(self, s: str) -> int:

        ch = s[0]
        current_index = 0
        
        arithmetic_set = []

        current_number = 0

        while current_index < len(s):
            ch = s[current_index]
            if ch == ' ':
                current_index += 1
                continue
            if ch in self.charToOpMap:
                arithmetic_set.append((current_number, ch))
                current_number = 0
            else:
                current_number = (current_number * 10) + int(ch)
            current_index += 1

        arithmetic_set.append((current_number, 'lmaooo')) # last element
        index_removal = set()
        arithmetic_set = self.evaluateOp(arithmetic_set, '/', '*')
        arithmetic_set = self.evaluateOp(arithmetic_set, '+', '-')


        return arithmetic_set[0][0]
        