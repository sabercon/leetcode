from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            while 0 <= n - 1 < i and nums[n - 1] != n:
                nums[n - 1], nums[i] = n, nums[n - 1]
                n = nums[i]
        for i, n in enumerate(nums):
            if i + 1 != n:
                return i + 1
        return len(nums) + 1
