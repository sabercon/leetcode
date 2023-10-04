from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plots = len(flowerbed)
        left_empty = True
        for i in range(plots):
            mid_empty = flowerbed[i] == 0
            right_empty = i == plots - 1 or flowerbed[i + 1] == 0
            if left_empty and mid_empty and right_empty:
                n -= 1
                left_empty = False
            else:
                left_empty = mid_empty
        return n <= 0
