from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {s: set() for s in stones}
        dp[0].add(0)
        for s in stones:
            for k in dp[s]:
                for nk in (k - 1, k, k + 1):
                    if nk > 0 and s + nk in dp:
                        dp[s + nk].add(nk)
        return bool(dp[stones[-1]])
