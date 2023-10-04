from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        p_with_stock, p_without_stock = float('-inf'), 0
        for price in prices:
            p_with_stock, p_without_stock = \
                max(p_with_stock, p_without_stock - price - fee), max(p_without_stock, p_with_stock + price)
        return p_without_stock
