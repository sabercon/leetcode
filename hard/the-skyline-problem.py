import heapq
from collections import defaultdict
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        building_map = defaultdict(list)
        for left, right, height in buildings:
            building_map[left].append((height, right))

        heap = [(0, 2 ** 31)]
        ans = []
        for i in sorted({i for left, right, _ in buildings for i in (left, right)}):
            while i >= heap[0][1]:
                heapq.heappop(heap)
            for height, right in building_map[i]:
                heapq.heappush(heap, (-height, right))

            if not ans or ans[-1][1] != -heap[0][0]:
                ans.append([i, -heap[0][0]])
        return ans
