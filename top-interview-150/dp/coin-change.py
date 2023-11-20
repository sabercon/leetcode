from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(num: int) -> int:
            if num == 0:
                return 0
            if num < 0:
                return amount + 1
            return min(dp(num - coin) for coin in coins) + 1

        return dp(amount) if dp(amount) <= amount else -1
