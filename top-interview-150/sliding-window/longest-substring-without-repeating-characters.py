class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        char_map = {}
        ans = 0
        for i, c in enumerate(s):
            start = max(start, char_map.get(c, -1) + 1)
            char_map[c] = i
            ans = max(ans, i - start + 1)
        return ans
