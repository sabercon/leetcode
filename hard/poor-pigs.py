from math import log2, ceil


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log2(buckets) / log2(minutesToTest // minutesToDie + 1))
