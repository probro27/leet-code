class Solution:
    def integer_divide_towards_zero(self, a, b):
        return -(-a // b) if (a < 0) ^ (b < 0) else a // b
    def evalRPN(self, tokens: List[str]) -> int:
        stack: [int] = []
        for element in tokens:
            result = re.match("[-+]?\d+$", element)
            if result is not None:
                stack.append(int(element))
            else:
                if element == "+":
                    length = len(stack)
                    stack[length - 2] = stack[length - 2] + stack[length - 1]
                    stack.pop()
                elif element == '-':
                    length = len(stack)
                    stack[length - 2] = stack[length - 2] - stack[length - 1]
                    stack.pop()
                elif element == '*':
                    length = len(stack)
                    stack[length - 2] = stack[length - 2] * stack[length - 1]
                    stack.pop()
                elif element == '/':
                    length = len(stack)
                    stack[length - 2] = self.integer_divide_towards_zero(stack[length-2], stack[length - 1])
                    stack.pop()
        return stack[0]