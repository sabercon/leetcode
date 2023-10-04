from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = Counter(tuple(row) for row in grid)
        return sum(row_counter[col] for col in zip(*grid))
