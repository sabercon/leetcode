from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Uses the minimum subarray sum to find the maximum circular subarray sum.
        """

        total = current_max = current_min = 0
        max_sum = min_sum = nums[0]
        for num in nums:
            total += num
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)
            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
