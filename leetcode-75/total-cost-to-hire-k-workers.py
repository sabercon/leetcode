import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = candidates - 1, len(costs) - candidates
        heap = [(cost, i) for i, cost in enumerate(costs) if i <= left or i >= right]
        heapq.heapify(heap)
        ans = 0
        for _ in range(k):
            cost, i = heapq.heappop(heap)
            ans += cost
            if i <= left < right - 1:
                left += 1
                heapq.heappush(heap, (costs[left], left))
            elif left + 1 < right <= i:
                right -= 1
                heapq.heappush(heap, (costs[right], right))
        return ans
