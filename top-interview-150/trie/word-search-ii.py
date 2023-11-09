from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def insert(self, word: str, i: int = 0) -> None:
        if i == len(word):
            self.word = word
            return
        if word[i] not in self.children:
            self.children[word[i]] = TrieNode()
        self.children[word[i]].insert(word, i + 1)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_root = TrieNode()
        for word in words:
            trie_root.insert(word)

        m, n = len(board), len(board[0])
        ans = []

        def dfs(i: int, j: int, trie: TrieNode) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in trie.children:
                return

            next_trie = trie.children[board[i][j]]
            if next_trie.word:
                ans.append(next_trie.word)
                next_trie.word = None

            c = board[i][j]
            board[i][j] = '#'
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(i + di, j + dj, next_trie)
            board[i][j] = c

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie_root)

        return ans
