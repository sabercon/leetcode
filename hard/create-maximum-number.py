from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_number(nums: List[int], n: int) -> List[int]:
            stack = []
            for i, num in enumerate(nums):
                while len(stack) + len(nums) - i > n and stack and stack[-1] < num:
                    stack.pop()
                if len(stack) < n:
                    stack.append(num)
            return stack

        def merge_numbers(num1: List[int], num2: List[int]) -> List[int]:
            i1 = i2 = 0
            merged = []
            while i1 < len(num1) or i2 < len(num2):
                if greater(num1, i1, num2, i2):
                    merged.append(num1[i1])
                    i1 += 1
                else:
                    merged.append(num2[i2])
                    i2 += 1
            return merged

        def greater(num1: List[int], i1: int, num2: List[int], i2: int) -> bool:
            while i1 < len(num1) and i2 < len(num2) and num1[i1] == num2[i2]:
                i1 += 1
                i2 += 1
            return i1 < len(num1) and (i2 >= len(num2) or num1[i1] > num2[i2])

        ans = []
        for k1 in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            k2 = k - k1
            max_num = merge_numbers(max_number(nums1, k1), max_number(nums2, k2))
            ans = max(ans, max_num)
        return ans
