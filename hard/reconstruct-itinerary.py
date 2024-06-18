from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Graph is hard.
        """

        graph = defaultdict(list)
        for fr, to in sorted(tickets, reverse=True):
            graph[fr].append(to)
        itinerary = []

        def dfs(departure: str):
            while graph[departure]:
                # The loop can execute up to a maximum of 2 iterations.
                dfs(graph[departure].pop())
            itinerary.append(departure)

        dfs('JFK')
        return itinerary[::-1]
