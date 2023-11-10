from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(path: List[int]) -> None:
            if len(path) > k:
                ans.append(path[1:])
                return
            for i in range(path[-1] + 1, n + 1):
                path.append(i)
                backtrack(path)
                path.pop()

        backtrack([0])
        return ans
