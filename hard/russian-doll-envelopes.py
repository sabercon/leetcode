from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        heights = []
        for _, h in sorted(envelopes, key=lambda e: (e[0], -e[1])):
            i = bisect_left(heights, h)
            if i == len(heights):
                heights.append(h)
            else:
                heights[i] = h
        return len(heights)
