from functools import cache


class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def is_palindrome(start: int, end: int) -> bool:
            return True if start >= end else s[start] == s[end] and is_palindrome(start + 1, end - 1)

        dp = [-1]
        for i in range(len(s)):
            dp.append(min(dp[j] + 1 for j in range(i + 1) if is_palindrome(j, i)))
        return dp[-1]
