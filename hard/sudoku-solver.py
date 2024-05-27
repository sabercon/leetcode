from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        mask_row = [0] * 9
        mask_col = [0] * 9
        mask_box = [0] * 9

        def is_valid(x: int, y: int, num: int) -> bool:
            mask = 1 << num
            return (mask_row[x] & mask > 0) or (mask_col[y] & mask > 0) or (mask_box[x - x % 3 + y // 3] & mask > 0)

        def add(x: int, y: int, num: int):
            board[x][y] = str(num)
            mask = 1 << num
            mask_row[x] |= mask
            mask_col[y] |= mask
            mask_box[x - x % 3 + y // 3] |= mask

        def remove(x: int, y: int, num: int):
            board[x][y] = '.'
            mask = 1 << num
            mask_row[x] ^= mask
            mask_col[y] ^= mask
            mask_box[x - x % 3 + y // 3] ^= mask

        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    add(i, j, int(c))

        def solve(x: int, y: int) -> bool:
            if x > 8:
                return True
            if y > 8:
                return solve(x + 1, 0)
            if board[x][y] != '.':
                return solve(x, y + 1)
            for num in range(1, 10):
                if is_valid(x, y, num):
                    continue
                add(x, y, num)
                if solve(x, y + 1):
                    return True
                remove(x, y, num)
            return False

        assert solve(0, 0)
