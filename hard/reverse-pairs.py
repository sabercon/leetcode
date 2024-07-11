from typing import List, Tuple


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def divide_and_conquer(start: int, end: int) -> Tuple[int, List[int]]:
            if end - start == 1:
                return 0, [nums[start]]
            mid = (start + end) // 2
            left_pairs, left_sorted = divide_and_conquer(start, mid)
            right_pairs, right_sorted = divide_and_conquer(mid, end)
            pairs = left_pairs + right_pairs
            j = 0
            for i, n in enumerate(left_sorted):
                while j < len(right_sorted) and right_sorted[j] * 2 < n:
                    j += 1
                pairs += j
            return pairs, sorted(left_sorted + right_sorted)

        return divide_and_conquer(0, len(nums))[0]
