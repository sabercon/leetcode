from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(largest_sum: int) -> bool:
            i = t = 0
            for n in nums:
                t += n
                if t > largest_sum:
                    t = n
                    i += 1
                    if t > largest_sum or i >= k:
                        return False
            return True

        mi, ma = 0, sum(nums)
        while mi < ma:
            mid = (mi + ma) // 2
            if can_split(mid):
                ma = mid
            else:
                mi = mid + 1
        return mi
