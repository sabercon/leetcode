import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        heap = []
        seen = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    seen.add((i, j))

        ans = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    ans += max(0, h - heightMap[ni][nj])
                    heapq.heappush(heap, (max(h, heightMap[ni][nj]), ni, nj))
                    seen.add((ni, nj))
        return ans
