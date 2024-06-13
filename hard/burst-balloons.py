from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums + [1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i, -1, -1):
                dp[j][i] = max(nums[k] * nums[j - 1] * nums[i + 1] + dp[j][k - 1] + dp[k + 1][i]
                               for k in range(j, i + 1))
        return dp[0][n - 1]
