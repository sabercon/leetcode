class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''.join(a + b for a, b in zip(word1, word2))
        remaining = word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):]
        return merged + remaining
