from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)

        @cache
        def is_match(si: int, pi: int) -> bool:
            if pi == pn:
                return si == sn
            if si == sn:
                return all(p[i] == '*' for i in range(pi, pn))
            match p[pi]:
                case '*':
                    return is_match(si, pi + 1) or is_match(si + 1, pi)
                case '?':
                    return is_match(si + 1, pi + 1)
                case c:
                    return s[si] == c and is_match(si + 1, pi + 1)

        return is_match(0, 0)
