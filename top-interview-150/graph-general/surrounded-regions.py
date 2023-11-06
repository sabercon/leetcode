from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        uncaptured = set()

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in uncaptured or board[i][j] == 'X':
                return
            uncaptured.add((i, j))
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(i + di, j + dj)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if (i, j) not in uncaptured:
                    board[i][j] = 'X'
