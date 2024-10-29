class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        paranthesisToRemove = []

        for index, ch in enumerate(s):
            if ch == '(':
                stack.append(index)
            elif ch == ')':
                if len(stack) == 0:
                    paranthesisToRemove.append(index)
                else:
                    stack.pop()
        
        if len(stack) != 0:
            paranthesisToRemove.extend(stack)

        paranthesisToRemove.sort(reverse=True)

        final_string = ''

        currentParanthesisIndex = 0
        for index, ch in enumerate(s[::-1]):
            actual_index = len(s) - index - 1
            if currentParanthesisIndex >= len(paranthesisToRemove) or (actual_index != paranthesisToRemove[currentParanthesisIndex]):
                final_string += ch
            else:
                currentParanthesisIndex += 1
        
        return final_string[::-1]

