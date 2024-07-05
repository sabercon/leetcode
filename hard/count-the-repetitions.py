class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        l1, l2 = len(s1), len(s2)
        dp = {(0, 0): (0, 0)}
        i1 = i2 = 0
        while i1 < n1 * l1:
            if s1[i1 % l1] == s2[i2 % l2]:
                i2 += 1
            i1 += 1

            j1, j2 = i1 % l1, i2 % l2
            if (j1, j2) in dp:
                last_i1, last_i2 = dp[(j1, j2)]
                if i2 == last_i2:
                    return 0
                times = (n1 * l1 - i1) // (i1 - last_i1)
                i1 += times * (i1 - last_i1)
                i2 += times * (i2 - last_i2)
            else:
                dp[(j1, j2)] = (i1, i2)

        return i2 // (n2 * l2)
