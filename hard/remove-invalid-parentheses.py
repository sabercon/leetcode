from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = set()

        def backtrack(t: str, i: int, left: int, right: int, to_remove: int, unmatched: int):
            pair_to_remove = to_remove - abs(left + unmatched - right)
            if to_remove < 0 or unmatched < 0 or unmatched > right or pair_to_remove < 0 or pair_to_remove % 2 != 0:
                return
            if i == len(s):
                ans.add(t)
            elif s[i] == '(':
                backtrack(t, i + 1, left - 1, right, to_remove - 1, unmatched)
                backtrack(t + s[i], i + 1, left - 1, right, to_remove, unmatched + 1)
            elif s[i] == ')':
                backtrack(t, i + 1, left, right - 1, to_remove - 1, unmatched)
                backtrack(t + s[i], i + 1, left, right - 1, to_remove, unmatched - 1)
            else:
                backtrack(t + s[i], i + 1, left, right, to_remove, unmatched)

        total_left = total_right = min_removed = unmatched_left = 0
        for c in s:
            if c == '(':
                total_left += 1
                unmatched_left += 1
            if c == ')':
                total_right += 1
                if unmatched_left > 0:
                    unmatched_left -= 1
                else:
                    min_removed += 1
        min_removed += unmatched_left
        backtrack('', 0, total_left, total_right, min_removed, 0)
        return list(ans)
