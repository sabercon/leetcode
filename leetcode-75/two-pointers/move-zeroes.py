from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j, n in enumerate(nums):
            if n != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
