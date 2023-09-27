from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        outs = [[] for _ in range(n)]
        ins = [[] for _ in range(n)]
        for u, v in connections:
            outs[u].append(v)
            ins[v].append(u)

        def dfs(u: int, p: int) -> int:
            return sum(1 + dfs(v, u) for v in outs[u] if v != p) + sum(dfs(v, u) for v in ins[u] if v != p)

        return dfs(0, -1)
