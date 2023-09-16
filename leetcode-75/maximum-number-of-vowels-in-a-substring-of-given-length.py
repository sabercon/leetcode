class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        ans = count = sum(s[i] in vowels for i in range(k))
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i - k] in vowels)
            ans = max(ans, count)
        return ans
