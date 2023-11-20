from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i: int) -> bool:
            if i == len(s):
                return True
            return any(dp(i + len(word)) for word in wordDict if s.startswith(word, i))

        return dp(0)
