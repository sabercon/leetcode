from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0] + [float('inf')] * len(grid[0])
        for row in grid:
            for i, num in enumerate(row):
                dp[i] = num + min(dp[i - 1], dp[i])
        return dp[-2]
