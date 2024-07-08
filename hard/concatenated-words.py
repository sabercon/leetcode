from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        word_set = set(words)
        for word in words:
            dp = [False] * len(word)
            for i in range(len(word)):
                dp[i] = ((i + 1 != len(word) and word[:i + 1] in word_set)
                         or any(dp[j] and word[j + 1:i + 1] in word_set for j in range(i)))
            if dp[-1]:
                ans.append(word)
        return ans
