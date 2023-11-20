class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp1 = dp2 = list(range(n))
        for size in range(n + 1):
            dp = [i - 1 for i in dp1 if i - 1 >= 0 and i + size < n and s[i - 1] == s[i + size]]
            if not dp2 and not dp:
                return s[dp1[0]:dp1[0] + size]
            dp1, dp2 = dp2, dp
        raise AssertionError
