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


class Solution2:
    def decodeString(self, s: str) -> str:
        strs = ['']
        nums = [0]
        for c in s:
            if c.isdigit():
                nums[-1] = nums[-1] * 10 + int(c)
            elif c.isalpha():
                strs[-1] += c
            elif c == '[':
                strs.append('')
                nums.append(0)
            elif c == ']':
                decoded = strs.pop() * nums.pop(-2)
                strs[-1] += decoded
        assert len(strs) == 1
        return strs[0]
