from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        def live_neighbors(x: int, y: int) -> int:
            return sum(board[x + dx][y + dy] % 2 for dx in range(-1, 2) for dy in range(-1, 2)
                       if 0 <= x + dx < m and 0 <= y + dy < n and (dx or dy))

        for i in range(m):
            for j in range(n):
                live = live_neighbors(i, j)
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 1:
                    board[i][j] = 1 - board[i][j] % 2
