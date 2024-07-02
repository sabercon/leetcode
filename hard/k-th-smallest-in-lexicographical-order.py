class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix: int) -> int:
            total = 0
            low, high = prefix, prefix + 1
            while low <= n:
                total += min(high, n + 1) - low
                low *= 10
                high *= 10
            return total

        ans = 1
        while k > 1:
            count = count_prefix(ans)
            if k <= count:
                k -= 1
                ans *= 10
            else:
                k -= count
                ans += 1
        return ans
