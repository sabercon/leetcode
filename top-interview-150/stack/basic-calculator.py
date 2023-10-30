class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result, num, sign = 0, 0, 1
        for c in s:
            match c:
                case ' ':
                    continue
                case '(':
                    stack.append((result, sign))
                    result = 0
                    sign = 1
                case ')':
                    (last_result, last_sign) = stack.pop()
                    result = last_result + (result + num * sign) * last_sign
                    num = 0
                case '+' | '-':
                    result += num * sign
                    num = 0
                    sign = 1 if c == '+' else -1
                case _:
                    num = num * 10 + int(c)
        return result + num * sign
