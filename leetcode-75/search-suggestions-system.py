from bisect import bisect_left
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = [[] for _ in range(len(searchWord))]
        for i in range(len(searchWord)):
            prefix = searchWord[:i + 1]
            j = bisect_left(products, prefix)
            while j < len(products) and products[j].startswith(prefix) and len(ans[i]) < 3:
                ans[i].append(products[j])
                j += 1
        return ans
