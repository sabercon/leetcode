class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replacement, used = {}, set()
        for sc, tc in zip(s, t):
            if sc in replacement:
                if replacement[sc] != tc:
                    return False
            elif tc in used:
                return False
            else:
                replacement[sc] = tc
                used.add(tc)
        return True


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
