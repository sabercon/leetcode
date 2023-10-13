from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * len(ratings)
        for i, r in sorted(enumerate(ratings), key=lambda ir: ir[1]):
            candies[i] = 1
            if i > 0 and ratings[i - 1] < r:
                candies[i] = max(candies[i], candies[i - 1] + 1)
            if i < len(ratings) - 1 and ratings[i + 1] < r:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
