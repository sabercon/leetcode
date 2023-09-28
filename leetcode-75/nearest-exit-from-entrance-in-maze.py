from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = {(entrance[0], entrance[1])}
        while queue:
            x, y, step = queue.popleft()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return step + 1
                    queue.append((nx, ny, step + 1))
                    visited.add((nx, ny))
        return -1
