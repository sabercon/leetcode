from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        def count(start: int, end: int):
            if end - start < 2:
                return
            mid = (start + end) // 2
            count(start, mid)
            count(mid, end)
            right_half = sorted(nums[mid:end])
            for i in range(start, mid):
                ans[i] += bisect_left(right_half, nums[i])

        count(0, len(nums))
        return ans
