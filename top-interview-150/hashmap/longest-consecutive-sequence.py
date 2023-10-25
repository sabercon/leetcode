from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num - 1 in nums:
                continue
            next_num = num + 1
            while next_num in nums:
                next_num += 1
            ans = max(ans, next_num - num)
        return ans
