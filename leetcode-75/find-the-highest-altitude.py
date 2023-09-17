from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = altitude = 0
        for g in gain:
            altitude += g
            ans = max(ans, altitude)
        return ans
