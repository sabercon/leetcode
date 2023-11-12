from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i: int, j: int, k: int) -> bool:
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            board[i][j] = '#'
            ans = any(backtrack(i + di, j + dj, k + 1) for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)))
            board[i][j] = word[k]
            return ans

        return any(backtrack(i, j, 0) for i in range(m) for j in range(n))
