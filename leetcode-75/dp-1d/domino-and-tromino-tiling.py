class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        even1, even2, uneven = 1, 0, 0
        for _ in range(n):
            even1, even2, uneven = (even1 + even2 + 2 * uneven) % mod, even1, (even2 + uneven) % mod
        return even1
