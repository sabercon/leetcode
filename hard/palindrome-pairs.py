from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        word_map = {w[::-1]: i for i, w in enumerate(words)}
        ans = []
        for i, word in enumerate(words):
            for j in range(1, len(word)):
                left, right = word[:j], word[j:]
                if right in word_map and is_palindrome(left):
                    ans.append([word_map[right], i])
                if left in word_map and is_palindrome(right):
                    ans.append([i, word_map[left]])
            if word in word_map and i != word_map[word]:
                ans.append([i, word_map[word]])
            if word != '' and '' in word_map and is_palindrome(word):
                ans.append([i, word_map['']])
                ans.append([word_map[''], i])
        return ans
