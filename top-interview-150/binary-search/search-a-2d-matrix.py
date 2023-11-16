from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // n][mid % n]
            if val < target:
                low = mid + 1
            elif val > target:
                high = mid - 1
            else:
                return True
        return False
