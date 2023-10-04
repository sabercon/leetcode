from typing import List, Tuple


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        roots = {}
        weights = {}

        def find(var: str) -> Tuple[str, float]:
            root, value = roots[var]
            if root != var:
                root, root_value = find(root)
                value *= root_value
            return root, value

        def union(a: str, b: str, value: float) -> None:
            if weights[a] > weights[b]:
                a, b = b, a
                value = 1.0 / value
            weights[b] += weights[a]
            roots[a] = (b, value)

        def query(a: str, b: str) -> float:
            if a not in roots or b not in roots:
                return -1.0
            a_root, a_value = find(a)
            b_root, b_value = find(b)
            if a_root != b_root:
                return -1.0
            return a_value / b_value

        for (a, b), v in zip(equations, values):
            for var in (a, b):
                if var not in roots:
                    roots[var] = (var, 1.0)
                    weights[var] = 1
            a_root, a_value = find(a)
            b_root, b_value = find(b)
            if a_root != b_root:
                union(a_root, b_root, v * b_value / a_value)

        return [query(a, b) for a, b in queries]
