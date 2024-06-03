class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] + [0] * len(t)
        for c in s:
            for i in range(len(t) - 1, -1, -1):
                if c == t[i]:
                    dp[i + 1] += dp[i]
        return dp[-1]
