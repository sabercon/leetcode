from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        inf = 2 ** 31 - 1
        n = len(dungeon[0])
        dp = [inf] * (n - 1) + [1]
        for row in reversed(dungeon):
            new_dp = [0] * n + [inf]
            for i in range(n - 1, -1, -1):
                new_dp[i] = max(min(new_dp[i + 1], dp[i]) - row[i], 1)
            dp = new_dp
        return dp[0]
