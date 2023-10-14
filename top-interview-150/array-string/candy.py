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


class Solution2:
    def candy(self, ratings: List[int]) -> int:
        candies = last_peak = desc_size = 1
        for i in range(1, len(ratings)):
            if ratings[i] < ratings[i - 1]:
                candies += desc_size if last_peak > desc_size else desc_size + 1
                desc_size += 1
                last_peak = max(last_peak, desc_size)
            else:
                if ratings[i] == ratings[i - 1]:
                    last_peak = 1
                else:
                    last_peak = last_peak + 1 if desc_size == 1 else 2
                desc_size = 1
                candies += last_peak
        return candies
