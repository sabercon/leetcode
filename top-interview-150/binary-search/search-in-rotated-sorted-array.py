from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        first_val = nums[0]
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            if first_val <= mid_val < target or target < first_val <= mid_val or mid_val < target < first_val:
                left = mid + 1
            else:
                right = mid - 1
        return -1
