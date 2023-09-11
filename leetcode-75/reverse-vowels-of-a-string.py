class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [(i, c) for i, c in enumerate(s) if c in 'aeiouAEIOU']
        reversed_vowels = {i: c for (_, c), (i, _) in zip(vowels, reversed(vowels))}
        return ''.join(reversed_vowels.get(i, c) for i, c in enumerate(s))
