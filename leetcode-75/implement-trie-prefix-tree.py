class Trie:

    def __init__(self):
        self.tree = [None] * 27

    def insert(self, word: str) -> None:
        tree = self.tree
        for c in word:
            i = self._index(c)
            if not tree[i]:
                tree[i] = [None] * 27
            tree = tree[i]
        tree[-1] = True

    def search(self, word: str) -> bool:
        tree = self.tree
        for c in word:
            i = self._index(c)
            if not tree[i]:
                return False
            tree = tree[i]
        return bool(tree[-1])

    def startsWith(self, prefix: str) -> bool:
        tree = self.tree
        for c in prefix:
            i = self._index(c)
            if not tree[i]:
                return False
            tree = tree[i]
        return True

    @staticmethod
    def _index(char: str) -> int:
        return ord(char) - ord('a')
