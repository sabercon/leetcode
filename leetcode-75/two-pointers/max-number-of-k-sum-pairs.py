from collections import Counter
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


class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        ans = 0
        for num, count in counts.items():
            if num * 2 == k:
                ans += count - count % 2
            else:
                ans += min(count, counts[k - num])
        return ans // 2
