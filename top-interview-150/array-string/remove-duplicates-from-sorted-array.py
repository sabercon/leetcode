from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        ans = 0
        for num in nums:
            if num != prev:
                nums[ans] = num
                ans += 1
                prev = num
        return ans
