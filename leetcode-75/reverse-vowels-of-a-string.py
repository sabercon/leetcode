class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [(i, c) for i, c in enumerate(s) if c in 'aeiouAEIOU']
        reversed_vowels = {i: c for (_, c), (i, _) in zip(vowels, reversed(vowels))}
        return ''.join(reversed_vowels.get(i, c) for i, c in enumerate(s))


class Solution2:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        start, end = 0, len(s) - 1
        while start < end:
            if chars[start] not in 'aeiouAEIOU':
                start += 1
            elif chars[end] not in 'aeiouAEIOU':
                end -= 1
            else:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1
        return ''.join(chars)
