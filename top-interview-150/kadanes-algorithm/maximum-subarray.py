from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        current = 0
        for num in nums:
            current = max(current + num, num)
            ans = max(ans, current)
        return ans
