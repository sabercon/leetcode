from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or (i, j) in seen:
                return
            seen.add((i, j))
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(i + di, j + dj)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    dfs(i, j)
                    ans += 1
        return ans
