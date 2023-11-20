from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [1] + [0] * len(obstacleGrid[0])
        for row in obstacleGrid:
            for i, obstacle in enumerate(row):
                dp[i] = 0 if obstacle else dp[i] + dp[i - 1]
        return dp[-2]
