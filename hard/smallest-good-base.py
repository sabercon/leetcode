from math import ceil, floor, log


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        for i in range(num.bit_length(), 2, -1):
            low, high = ceil(num ** (1 / i)), floor(num ** (1 / (i - 1)))
            while low <= high:
                mid = (low + high) // 2
                value = 0
                for _ in range(i):
                    value = value * mid + 1
                if value == num:
                    return str(mid)
                if value < num:
                    low = mid + 1
                else:
                    high = mid - 1
        return str(num - 1)


class Solution2:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for i in range(int(log(n, 2)), 1, -1):
            k = int(n ** (1 / i))
            if (k ** (i + 1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)
