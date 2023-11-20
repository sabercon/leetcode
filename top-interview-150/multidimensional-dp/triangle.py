from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for row in triangle[-2::-1]:
            dp = [num + min(dp[i], dp[i + 1]) for i, num in enumerate(row)]
        return dp[0]
