from functools import cache


class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        if len(p) > 1 and p[1] == '*':
            return (self.is_match_on_first_char(s, p) and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
        return self.is_match_on_first_char(s, p) and self.isMatch(s[1:], p[1:])

    def is_match_on_first_char(self, s: str, p: str) -> bool:
        return s and p and (s[0] == p[0] or p[0] == '.')
