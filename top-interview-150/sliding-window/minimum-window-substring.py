from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        expected = Counter(t)
        expected_count = len(t)
        left = 0
        ans = (-1, len(s) - 1)
        for right, char in enumerate(s, start=1):
            expected[char] -= 1
            if expected[char] >= 0:
                expected_count -= 1
            while left < right and expected[s[left]] < 0:
                expected[s[left]] += 1
                left += 1
            if expected_count == 0 and right - left <= ans[1] - ans[0]:
                ans = (left, right)
        return s[ans[0]:ans[1]]
