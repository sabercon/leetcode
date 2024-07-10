import heapq
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(small: list[tuple[int, int]], large: list[tuple[int, int]]) -> float:
            return -small[0][0] if k % 2 else (-small[0][0] + large[0][0]) / 2

        def move(fr: list[tuple[int, int]], to: list[tuple[int, int]]):
            num, index = heapq.heappop(fr)
            heapq.heappush(to, (-num, index))

        small_heap, large_heap = [(-n, i) for i, n in enumerate(nums[:k])], []
        heapq.heapify(small_heap)
        for _ in range(k // 2):
            move(small_heap, large_heap)

        ans = [median(small_heap, large_heap)]
        for i, n in enumerate(nums[k:]):
            if n <= -small_heap[0][0]:
                heapq.heappush(small_heap, (-n, i + k))
                if nums[i] >= -small_heap[0][0]:
                    move(small_heap, large_heap)
            else:
                heapq.heappush(large_heap, (n, i + k))
                if nums[i] <= large_heap[0][0]:
                    move(large_heap, small_heap)

            for h in (small_heap, large_heap):
                while h and h[0][1] <= i:
                    heapq.heappop(h)
            ans.append(median(small_heap, large_heap))
        return ans
