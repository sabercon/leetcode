from collections import Counter
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p1: List[int], p2: List[int]) -> float:
            x1, y1 = p1
            x2, y2 = p2
            if x1 == x2:
                return float('inf')
            return (y2 - y1) / (x2 - x1)

        ans = 1
        for i, p1 in enumerate(points[:-1]):
            counter = Counter(slope(p1, p2) for p2 in points[i + 1:])
            ans = max(ans, counter.most_common(1)[0][1] + 1)
        return ans
