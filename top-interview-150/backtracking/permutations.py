from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        return [p + [nums[i]] for i in range(len(nums)) for p in self.permute(nums[:i] + nums[i + 1:])]
