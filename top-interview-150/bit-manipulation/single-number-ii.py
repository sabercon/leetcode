from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # mask: 00 -> 01 -> 10 -> 00
        mask1 = mask2 = 0
        for num in nums:
            mask2 ^= num & ~mask1
            mask1 ^= num & ~mask2
        return mask1 ^ mask2
