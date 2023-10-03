from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n1 = n2 = 0
        for n in nums:
            n1, n2 = n2, max(n1 + n, n2)
        return n2
