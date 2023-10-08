from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i1, i2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if i2 < 0 or (i1 >= 0 and nums1[i1] > nums2[i2]):
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
