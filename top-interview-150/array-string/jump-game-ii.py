from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end = 0, 1
        k = 0
        while end < len(nums):
            start, end = end, max(i + nums[i] for i in range(start, end)) + 1
            k += 1
        return k
