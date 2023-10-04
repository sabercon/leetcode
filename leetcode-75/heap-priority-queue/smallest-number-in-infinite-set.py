import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.num = 1
        self.num_set = set()
        self.num_heap = []

    def popSmallest(self) -> int:
        if self.num_heap:
            ans = heapq.heappop(self.num_heap)
            self.num_set.remove(ans)
        else:
            ans = self.num
            self.num += 1
        return ans

    def addBack(self, num: int) -> None:
        if num < self.num and num not in self.num_set:
            heapq.heappush(self.num_heap, num)
            self.num_set.add(num)
