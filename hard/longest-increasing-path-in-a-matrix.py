from functools import cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(matrix), len(matrix[0])

        @cache
        def dfs(x: int, y: int) -> int:
            path = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    path = max(path, dfs(nx, ny))
            return path + 1

        return max(dfs(i, j) for i in range(m) for j in range(n))
