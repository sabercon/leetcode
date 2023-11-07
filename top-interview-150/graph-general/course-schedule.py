from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            degree[a] += 1

        stack = [i for i in range(numCourses) if degree[i] == 0]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    stack.append(neighbor)
        return count == numCourses
