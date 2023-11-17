from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_left(num: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            return left

        range_left = bisect_left(target)
        return [range_left, bisect_left(target + 1) - 1] if target in nums[range_left:range_left + 1] else [-1, -1]
