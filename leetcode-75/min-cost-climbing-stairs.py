from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost1 = cost2 = 0
        for c in cost:
            cost1, cost2 = cost2, min(cost1, cost2) + c
        return min(cost1, cost2)
