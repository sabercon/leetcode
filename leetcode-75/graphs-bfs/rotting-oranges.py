from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        fresh = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1}
        rotten = {(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2}
        minutes = 0
        while fresh:
            rotting = {(i, j) for i, j in fresh if any((i + di, j + dj) in rotten for di, dj in directions)}
            if not rotting:
                return -1
            fresh -= rotting
            rotten |= rotting
            minutes += 1
        return minutes
