from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def binary_search(i1: int, i2: int, rank: int) -> int:
            if i1 >= len(nums1):
                return nums2[i2 + rank - 1]
            if i2 >= len(nums2):
                return nums1[i1 + rank - 1]
            if rank == 1:
                return min(nums1[i1], nums2[i2])

            delta = rank // 2 - 1
            num1 = nums1[i1 + delta] if i1 + delta < len(nums1) else float('inf')
            num2 = nums2[i2 + delta] if i2 + delta < len(nums2) else float('inf')
            if num1 > num2:
                return binary_search(i1, i2 + delta + 1, rank - delta - 1)
            else:
                return binary_search(i1 + delta + 1, i2, rank - delta - 1)

        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return binary_search(0, 0, n // 2 + 1)
        else:
            return (binary_search(0, 0, n // 2) + binary_search(0, 0, n // 2 + 1)) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search is really hard.
        """

        m, n = len(nums1), len(nums2)
        after = (m + n - 1) // 2
        lo, hi = max(0, after - n), min(m, after)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums1[mid] >= nums2[after - mid - 1]:
                hi = mid
            else:
                lo = mid + 1

        i = lo
        next_nums = sorted(nums1[i:i + 2] + nums2[after - i:after - i + 2])
        return (next_nums[0] + next_nums[1 - (m + n) % 2]) / 2
