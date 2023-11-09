from collections import deque, defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                words[word[:i] + "_" + word[i + 1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, length = queue.popleft()
            for i in range(len(word)):
                for next_word in words[word[:i] + "_" + word[i + 1:]]:
                    if next_word in visited:
                        continue
                    if next_word == endWord:
                        return length + 1
                    queue.append((next_word, length + 1))
                    visited.add(next_word)
        return 0
