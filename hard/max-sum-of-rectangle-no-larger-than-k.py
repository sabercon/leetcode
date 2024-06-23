from bisect import bisect_left, insort
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = -2 ** 31
        for i1 in range(m):
            sums = [0] * (n + 1)
            for i2 in range(i1, m):
                current_sum = 0
                for j, num in enumerate(matrix[i2]):
                    current_sum += num
                    sums[j + 1] += current_sum

                sorted_sums = [0]
                for j1 in range(1, n + 1):
                    j2 = bisect_left(sorted_sums, sums[j1] - k)
                    if j2 < len(sorted_sums):
                        ans = max(ans, sums[j1] - sorted_sums[j2])
                    insort(sorted_sums, sums[j1])
        return ans
