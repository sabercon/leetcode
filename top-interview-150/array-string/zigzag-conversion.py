class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        i = 0
        step = 1 if numRows > 1 else 0
        for c in s:
            rows[i] += c
            i += step
            if i == 0 or i == numRows - 1:
                step *= -1
        return ''.join(rows)
