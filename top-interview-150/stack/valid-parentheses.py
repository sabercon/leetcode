class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            else:
                stack.append(c)
        return not stack
