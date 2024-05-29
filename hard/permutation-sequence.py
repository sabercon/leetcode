from math import factorial
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def get_permutation(nums: List[str], rank: int) -> str:
            if not nums:
                return ''
            f = factorial(len(nums) - 1)
            i = rank // f
            return nums[i] + get_permutation(nums[:i] + nums[i + 1:], rank % f)

        return get_permutation([str(i + 1) for i in range(n)], k - 1)
