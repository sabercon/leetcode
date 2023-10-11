from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i] < prices[i + 1])
