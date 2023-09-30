import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negated_nums = [-num for num in nums]
        heapq.heapify(negated_nums)
        for _ in range(k - 1):
            heapq.heappop(negated_nums)
        return -heapq.heappop(negated_nums)
