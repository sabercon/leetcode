from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        start_i = bisect_left(intervals, start, key=lambda i: i[0])
        end_i = bisect_right(intervals, end, key=lambda i: i[1])
        if start_i > 0 and intervals[start_i - 1][1] >= start:
            start_i -= 1
            start = intervals[start_i][0]
        if end_i < len(intervals) and intervals[end_i][0] <= end:
            end_i += 1
            end = intervals[end_i - 1][1]
        return intervals[:start_i] + [[start, end]] + intervals[end_i:]
