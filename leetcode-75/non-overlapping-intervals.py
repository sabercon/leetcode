from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        current_end = float('-inf')
        ans = 0
        for start, end in intervals:
            if start < current_end:
                ans += 1
            else:
                current_end = end
        return ans
