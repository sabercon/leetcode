from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        dp = [defaultdict(lambda: 0) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                ans += dp[j][diff]
        return ans
