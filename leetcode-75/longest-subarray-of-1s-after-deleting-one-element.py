from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        k = 1
        for n in nums:
            if n == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return len(nums) - i - 1
