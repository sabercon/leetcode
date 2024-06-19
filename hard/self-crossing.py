from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        distance.extend((0, 0))
        for i in range(3, len(distance) - 2):
            if distance[i - 1] > distance[i - 3]:
                continue
            if distance[i] >= distance[i - 2]:
                return True
            if (distance[i - 1] + distance[i - 5] >= distance[i - 3]
                    and distance[i - 4] < distance[i - 2] <= distance[i] + distance[i - 4]):
                return True
        return False
