from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * (len(matrix[0]) + 1)
        ans = 0
        for row in matrix:
            heights = [(h + 1 if c == '1' else 0) for h, c in zip(heights, row)] + [0]
            stack = [(-1, -1)]
            for i, h in enumerate(heights):
                while stack[-1][1] >= h:
                    ans = max(ans, stack.pop()[1] * (i - 1 - stack[-1][0]))
                stack.append((i, h))
        return ans
