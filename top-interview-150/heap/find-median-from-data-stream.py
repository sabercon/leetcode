import heapq


class MedianFinder:

    def __init__(self):
        self.low_heap = []
        self.high_heap = []

    def addNum(self, num: int) -> None:
        if len(self.low_heap) == len(self.high_heap):
            heapq.heappush(self.low_heap, -heapq.heappushpop(self.high_heap, num))
        else:
            heapq.heappush(self.high_heap, -heapq.heappushpop(self.low_heap, -num))

    def findMedian(self) -> float:
        if len(self.low_heap) == len(self.high_heap):
            return (self.high_heap[0] - self.low_heap[0]) / 2.0
        return -self.low_heap[0]
