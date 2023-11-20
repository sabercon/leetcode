from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [-1000] * k
        sell = [0] * (k + 1)
        for price in prices:
            for i in range(k):
                buy[i] = max(buy[i], sell[i] - price)
                sell[i + 1] = max(sell[i + 1], buy[i] + price)
        return sell[-1]
