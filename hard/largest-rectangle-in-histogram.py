from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for height in heights + [-1]:
            width = 0
            while stack and stack[-1][0] >= height:
                h, w = stack.pop()
                width += w
                ans = max(ans, h * width)
            stack.append((height, width + 1))
        return ans
