from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set()

        def is_concatenated(word: str) -> bool:
            dp = [[False] * (len(word) + 1) for _ in range(len(word) + 1)]
            for i in range(1, len(word) + 1):
                for j in range(i - 1, -1, -1):
                    dp[j][i] = word[j:i] in word_set or any(dp[j][k] and dp[k][i] for k in range(j + 1, i))
            return dp[0][len(word)]

        ans = []
        for w in sorted(words, key=len):
            if is_concatenated(w):
                ans.append(w)
            else:
                word_set.add(w)
        return ans
