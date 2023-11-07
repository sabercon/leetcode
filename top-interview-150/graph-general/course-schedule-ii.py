from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            degree[a] += 1

        stack = [i for i in range(numCourses) if degree[i] == 0]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node)
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    stack.append(neighbor)
        return ans if len(ans) == numCourses else []
