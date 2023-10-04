import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums1, nums2), key=lambda n: -n[1])
        heap = [nums[i][0] for i in range(k)]
        heapq.heapify(heap)
        total = sum(heap)
        ans = total * nums[k - 1][1]

        for num1, num2 in nums[k:]:
            total += num1 - heapq.heappushpop(heap, num1)
            ans = max(ans, total * num2)
        return ans
