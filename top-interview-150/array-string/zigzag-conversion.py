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


class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        ans = []
        num = max(2 * numRows - 2, 1)
        for i in range(numRows):
            for j in range(0, len(s), num):
                if i + j < len(s):
                    ans.append(s[i + j])
                if i != 0 and i != numRows - 1 and num - i + j < len(s):
                    ans.append(s[num - i + j])
        return ''.join(ans)
