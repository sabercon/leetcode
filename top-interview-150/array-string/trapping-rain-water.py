from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        left_peak, right_peak = height[left], height[right]
        while left < right:
            if left_peak < right_peak:
                left += 1
                left_peak = max(left_peak, height[left])
                ans += left_peak - height[left]
            else:
                right -= 1
                right_peak = max(right_peak, height[right])
                ans += right_peak - height[right]
        return ans
