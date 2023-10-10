from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j, n in enumerate(nums):
            if n != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
