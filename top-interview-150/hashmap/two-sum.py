from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, n in enumerate(nums):
            if target - n in num_map:
                return [num_map[target - n], i]
            num_map[n] = i
        raise ValueError
