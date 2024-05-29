from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_mask = diag1_mask = diag2_mask = 0

        def backtrack(i: int) -> List[List[str]]:
            nonlocal col_mask, diag1_mask, diag2_mask

            if i == n:
                return [[]]

            ans = []
            for j in range(n):
                c_mask, d1_mask, d2_mask = 1 << j, 1 << (i + j), 1 << (i - j + n)
                if c_mask & col_mask or d1_mask & diag1_mask or d2_mask & diag2_mask:
                    continue
                col_mask |= c_mask
                diag1_mask |= d1_mask
                diag2_mask |= d2_mask
                row = ['.' * j + 'Q' + '.' * (n - j - 1)]
                ans.extend(row + solution for solution in backtrack(i + 1))
                col_mask ^= c_mask
                diag1_mask ^= d1_mask
                diag2_mask ^= d2_mask
            return ans

        return backtrack(0)
