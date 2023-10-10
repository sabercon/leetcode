from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Can use reversion to solve rotation problems.
        """

        def reverse(start: int, end: int) -> None:
            for i in range((end - start) // 2):
                nums[start + i], nums[end - i - 1] = nums[end - i - 1], nums[start + i]

        k = k % len(nums)
        reverse(0, len(nums))
        reverse(0, k)
        reverse(k, len(nums))
