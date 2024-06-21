from typing import List


class SummaryRanges:

    def __init__(self):
        self.seen = set()
        self.start_to_end = {}
        self.end_to_start = {}

    def addNum(self, value: int) -> None:
        if value in self.seen:
            return
        self.seen.add(value)

        start = end = value
        if value + 1 in self.start_to_end:
            end = self.start_to_end.pop(value + 1)
        if value - 1 in self.end_to_start:
            start = self.end_to_start.pop(value - 1)
        self.start_to_end[start] = end
        self.end_to_start[end] = start

    def getIntervals(self) -> List[List[int]]:
        return sorted([start, end] for start, end in self.start_to_end.items())
