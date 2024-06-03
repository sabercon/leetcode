from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def is_scramble(i1: int, i2: int, size: int) -> bool:
            if size < 2:
                return s1[i1:i1 + size] == s2[i2:i2 + size]
            for i in range(1, size):
                if ((is_scramble(i1, i2, i) and is_scramble(i1 + i, i2 + i, size - i))
                        or (is_scramble(i1, i2 + size - i, i) and is_scramble(i1 + i, i2, size - i))):
                    return True
            return False

        return is_scramble(0, 0, len(s1))
