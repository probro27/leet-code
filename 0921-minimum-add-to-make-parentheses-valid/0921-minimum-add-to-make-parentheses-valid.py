class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        changes = 0
        for ch in s:
            if ch == '(':
                stack.append('(')
            else:
                if len(stack) == 0:
                    changes += 1
                else:
                    stack.pop()
        
        return changes + len(stack)