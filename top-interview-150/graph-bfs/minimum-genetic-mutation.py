from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        visited = set()
        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            for next_gene in bank:
                if next_gene not in visited and sum(c1 != c2 for c1, c2 in zip(gene, next_gene)) == 1:
                    visited.add(next_gene)
                    queue.append((next_gene, mutations + 1))
        return -1
