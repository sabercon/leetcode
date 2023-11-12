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
