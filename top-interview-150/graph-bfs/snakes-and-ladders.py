from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_pos(num: int) -> (int, int):
            q, r = divmod(num - 1, n)
            return n - 1 - q, r if q % 2 == 0 else n - 1 - r

        queue = deque([(1, 0)])
        visited = set()
        while queue:
            num, step = queue.popleft()
            for i in range(1, 7):
                next_num = num + i
                x, y = get_pos(next_num)
                if board[x][y] != -1:
                    next_num = board[x][y]
                if next_num == n * n:
                    return step + 1
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, step + 1))
        return -1
