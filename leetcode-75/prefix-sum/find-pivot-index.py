from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, n in enumerate(nums):
            right -= n
            if left == right:
                return i
            left += n
        return -1
