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


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        si = pi = 0
        last_match = last_star = -1

        while si < len(s):
            if pi < len(p) and p[pi] == '*':
                pi += 1
                last_match = si
                last_star = pi
            elif pi < len(p) and (p[pi] == '?' or s[si] == p[pi]):
                pi += 1
                si += 1
            elif last_star > 0:
                last_match += 1
                si, pi = last_match, last_star
            else:
                return False

        return all(p[i] == '*' for i in range(pi, len(p)))
