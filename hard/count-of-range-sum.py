from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)

        def count_and_sort(start: int, end: int) -> int:
            if end - start == 1:
                return 0
            mid = (start + end) // 2
            ans = count_and_sort(start, mid) + count_and_sort(mid, end)
            left = right = mid
            for i in range(start, mid):
                while left < end and sums[left] - sums[i] < lower:
                    left += 1
                while right < end and sums[right] - sums[i] <= upper:
                    right += 1
                ans += right - left
            sums[start:end] = sorted(sums[start:end])
            return ans

        return count_and_sort(0, len(sums))
