import heapq
from collections import Counter
from typing import List


class Heap:
    def __init__(self, is_min_heap: bool):
        self._removed = Counter()
        self._nums = []
        self._size = 0
        self._is_min_heap = is_min_heap

    def top(self) -> int:
        return self._nums[0] if self._is_min_heap else -self._nums[0]

    def size(self) -> int:
        return self._size

    def push(self, num: int):
        heapq.heappush(self._nums, num if self._is_min_heap else -num)
        self._size += 1

    def pop(self) -> int:
        num = heapq.heappop(self._nums)
        self._size -= 1
        self._clean()
        return num if self._is_min_heap else -num

    def remove(self, num: int):
        self._removed[num if self._is_min_heap else -num] += 1
        self._size -= 1
        self._clean()

    def _clean(self):
        while self._nums and self._removed[self._nums[0]]:
            self._removed[heapq.heappop(self._nums)] -= 1


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        left_heap, right_heap = Heap(False), Heap(True)
        for i, num in enumerate(nums):
            if left_heap.size() and num <= left_heap.top():
                left_heap.push(num)
            else:
                right_heap.push(num)
            if left_heap.size() > right_heap.size() + 1:
                right_heap.push(left_heap.pop())
            if left_heap.size() < right_heap.size():
                left_heap.push(right_heap.pop())

            if i + 1 >= k:
                ans.append(left_heap.top() if k % 2 else (left_heap.top() + right_heap.top()) / 2)
                removed = nums[i + 1 - k]
                if removed <= left_heap.top():
                    left_heap.remove(removed)
                else:
                    right_heap.remove(removed)
        return ans
