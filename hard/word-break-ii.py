from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        @cache
        def build_sentences(i: int) -> List[str]:
            if i == len(s):
                return ['']
            ans = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in words:
                    ans.extend(f'{word} {sentence}' if sentence else word for sentence in build_sentences(j))
            return ans

        return build_sentences(0)
