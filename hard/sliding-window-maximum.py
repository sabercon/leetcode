from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for i, n in enumerate(nums):
            while queue and queue[-1][1] <= n:
                queue.pop()
            queue.append((i, n))
            if i >= k - 1:
                ans.append(queue[0][1])
            if i - queue[0][0] >= k - 1:
                queue.popleft()
        return ans
