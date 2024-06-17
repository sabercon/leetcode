from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m = i = ans = 0
        while m < n:
            if i < len(nums) and nums[i] <= m + 1:
                m += nums[i]
                i += 1
            else:
                m += m + 1
                ans += 1
        return ans
