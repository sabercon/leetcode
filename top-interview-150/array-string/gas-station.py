from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = end = tank = 0
        while end - start < len(gas):
            if tank + gas[end] - cost[end] < 0:
                start -= 1
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end += 1
        return start % len(gas) if tank >= 0 else -1
