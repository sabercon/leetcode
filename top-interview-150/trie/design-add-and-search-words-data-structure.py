class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.word_end = False

    def addWord(self, word: str) -> None:
        if not word:
            self.word_end = True
            return
        index = ord(word[0]) - ord('a')
        if not self.children[index]:
            self.children[index] = WordDictionary()
        self.children[index].addWord(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.word_end
        if word[0] == '.':
            return any(child.search(word[1:]) for child in self.children if child)
        index = ord(word[0]) - ord('a')
        return self.children[index] and self.children[index].search(word[1:])
