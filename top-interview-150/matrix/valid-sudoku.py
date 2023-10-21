from typing import List, Iterable


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(cells: Iterable[str]) -> bool:
            seen = set()
            for cell in cells:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
            return True

        for row in board:
            if not check(row):
                return False

        for col in zip(*board):
            if not check(col):
                return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not check(sub_box):
                    return False

        return True
