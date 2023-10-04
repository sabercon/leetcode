from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, cur_sum)
        return max_sum / k
