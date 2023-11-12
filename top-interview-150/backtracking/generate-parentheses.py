from functools import cache
from typing import List


class Solution:
    @cache
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        return [f'({p1}){p2}' for i in range(n)
                for p1 in self.generateParenthesis(i)
                for p2 in self.generateParenthesis(n - i - 1)]


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(acc: str, left: int, right: int):
            if right == 0:
                yield acc
            if left > 0:
                yield from generate(acc + '(', left - 1, right)
            if right > left:
                yield from generate(acc + ')', left, right - 1)

        return list(generate('', n, n))
