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


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            dp[i] = any(dp[j] and s[j:i] in wordDict for j in range(0, i))
        return dp[-1]
