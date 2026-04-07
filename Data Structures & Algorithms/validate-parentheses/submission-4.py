class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = { ')': '(', ']': '[', '}': '{' }

        for char in s:
            if char in matching:
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False