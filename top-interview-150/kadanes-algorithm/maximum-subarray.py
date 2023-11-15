from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        current = 0
        for num in nums:
            current = max(current + num, num)
            ans = max(ans, current)
        return ans


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_sub_array(left: int, right: int) -> (int, int, int, int):
            if left == right:
                return nums[left], nums[left], nums[left], nums[left]

            mid = (left + right) // 2
            left_max, left_total, left_left, left_right = max_sub_array(left, mid)
            right_max, right_total, right_left, right_right = max_sub_array(mid + 1, right)

            return max(left_max, right_max, left_right + right_left), left_total + right_total, \
                max(left_left, left_total + right_left), max(right_right, right_total + left_right)

        return max_sub_array(0, len(nums) - 1)[0]
