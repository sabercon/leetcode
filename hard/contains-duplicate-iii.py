from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        for i, n in enumerate(nums):
            if i > indexDiff:
                buckets.pop(nums[i - indexDiff - 1] // (valueDiff + 1))
            bucket = n // (valueDiff + 1)
            if (bucket in buckets
                    or (bucket - 1 in buckets and n - buckets[bucket - 1] <= valueDiff)
                    or (bucket + 1 in buckets and buckets[bucket + 1] - n <= valueDiff)):
                return True
            buckets[bucket] = n
        return False
