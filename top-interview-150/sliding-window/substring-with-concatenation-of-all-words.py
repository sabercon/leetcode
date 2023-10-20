from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0])
        word_count = len(words)
        word_counter = Counter(words)
        ans = []
        for i in range(word_size):
            left = right = i
            contained = Counter()
            while right + word_size <= len(s):
                word = s[right:right + word_size]
                right += word_size
                if word not in word_counter:
                    contained.clear()
                    left = right
                else:
                    contained[word] += 1
                    while contained[word] > word_counter[word]:
                        contained[s[left:left + word_size]] -= 1
                        left += word_size
                if right - left == word_size * word_count:
                    ans.append(left)
                    contained[s[left:left + word_size]] -= 1
                    left += word_size
        return ans
