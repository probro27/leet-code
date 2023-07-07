class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != '*':
                stack.append(ch)
            else:
                stack.pop()
        new_str = ""
        for char in stack:
            new_str = new_str + char
        return new_str