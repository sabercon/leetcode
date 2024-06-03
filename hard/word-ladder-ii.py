from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        paths = defaultdict(set)

        def build_paths(word: str) -> List[List[str]]:
            if word == beginWord:
                return [[beginWord]]
            return [path + [word] for next_word in paths[word] for path in build_paths(next_word)]

        word_masks = {}
        mask_words = defaultdict(set)
        for word in wordList + [beginWord]:
            word_masks[word] = [word[:i] + '_' + word[i + 1:] for i in range(len(word))]
            for mask in word_masks[word]:
                mask_words[mask].add(word)

        current_words = {beginWord}
        while current_words:
            next_words = set()
            for word in current_words:
                for mask in word_masks[word]:
                    mask_words[mask].remove(word)
            for word in current_words:
                for mask in word_masks[word]:
                    for w in mask_words[mask]:
                        paths[w].add(word)
                        next_words.add(w)
            if endWord in next_words:
                return build_paths(endWord)
            current_words = next_words
        return []
