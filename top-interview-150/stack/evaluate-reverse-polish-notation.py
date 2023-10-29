from operator import add, sub, mul, truediv
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': add, '-': sub, '*': mul, '/': truediv}
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                operand1, operand2 = stack.pop(), stack.pop()
                stack.append(int(ops[token](operand2, operand1)))
        return stack[0]
