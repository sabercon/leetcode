import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits), reverse=True)
        heap = []
        for _ in range(k):
            while projects and projects[-1][0] <= w:
                heapq.heappush(heap, -projects.pop()[1])
            if not heap:
                break
            w -= heapq.heappop(heap)
        return w
