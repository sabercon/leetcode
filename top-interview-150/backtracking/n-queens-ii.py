class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, diag1, diag2 = [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1)

        def backtrack(row: int) -> int:
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if cols[col] or diag1[row + col] or diag2[row - col]:
                    continue
                cols[col] = diag1[row + col] = diag2[row - col] = True
                count += backtrack(row + 1)
                cols[col] = diag1[row + col] = diag2[row - col] = False
            return count

        return backtrack(0)
