from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            n = nums[i] + nums[j]
            if n < k:
                i += 1
            elif n > k:
                j -= 1
            else:
                ans += 1
                i += 1
                j -= 1
        return ans
