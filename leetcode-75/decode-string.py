class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue

            chars = []
            while stack[-1] != '[':
                chars.append(stack.pop())
            stack.pop()
            string = ''.join(chars[::-1])

            digits = []
            while stack and stack[-1].isdigit():
                digits.append(stack.pop())
            number = int(''.join(digits[::-1]))

            stack.append(string * number)
        return ''.join(stack)
