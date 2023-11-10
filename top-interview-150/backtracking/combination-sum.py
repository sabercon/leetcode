from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if target < 0 or not candidates:
            return []
        return [[num] + c for i, num in enumerate(candidates)
                for c in self.combinationSum(candidates[i:], target - num)]
