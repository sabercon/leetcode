from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0] * (len(matrix[0]) + 1)
        ans = 0
        for row in matrix:
            temp = 0
            for i, num in enumerate(row):
                dp[i + 1], temp = min(dp[i + 1], dp[i], temp) + 1 if num == '1' else 0, dp[i + 1]
            ans = max(ans, max(dp))
        return ans ** 2
