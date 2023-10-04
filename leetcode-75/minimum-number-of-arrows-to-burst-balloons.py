from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        current_end = float('-inf')
        ans = 0
        for start, end in points:
            if start > current_end:
                ans += 1
                current_end = end
        return ans
