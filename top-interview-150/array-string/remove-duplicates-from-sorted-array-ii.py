from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev1 = prev2 = None
        ans = 0
        for num in nums:
            if num != prev1 or num != prev2:
                nums[ans] = num
                ans += 1
            prev1, prev2 = num, prev1
        return ans
