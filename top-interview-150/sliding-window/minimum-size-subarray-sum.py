from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        total = 0
        ans = len(nums) + 1
        for i, n in enumerate(nums):
            total += n
            while total - nums[start] >= target:
                total -= nums[start]
                start += 1
            if total >= target:
                ans = min(ans, i - start + 1)
        return ans if ans <= len(nums) else 0
