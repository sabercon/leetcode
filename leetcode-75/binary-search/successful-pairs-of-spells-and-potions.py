from bisect import bisect_left
from math import ceil
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        return [len(potions) - bisect_left(potions, ceil(success / spell)) for spell in spells]
