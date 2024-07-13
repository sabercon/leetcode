from math import ceil


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        top = 10 ** n - 1
        # For `n` in [2,8], a palindrome of length `2*n` exists.
        for left in range(top, top // 10, -1):
            p = int(str(left) + str(left)[::-1])
            for i in range(top, ceil(p ** 0.5) - 1, -1):
                if p % i == 0:
                    return p % 1337
        raise AssertionError
