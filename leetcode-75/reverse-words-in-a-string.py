class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


class Solution2:
    def reverseWords(self, s: str) -> str:
        """
        To mimic an O(1) space solution.
        Since strings are immutable in Python, we need to convert it to a list of characters first.
        """

        def reverse_and_move_word(idx: int, word_start: int, word_end: int) -> None:
            while word_end >= word_start and word_end > idx:
                s[idx], s[word_end] = s[word_end], s[idx]
                word_end -= 1
                idx += 1

        s = list(s)

        s.reverse()
        s.append(' ')
        cursor = -1
        start = -1
        for i, c in enumerate(s):
            if c != ' ' and start == -1:
                s[cursor] = ' '
                cursor += 1
                start = i
            if c == ' ' and start != -1:
                reverse_and_move_word(cursor, start, i - 1)
                cursor += i - start
                start = -1

        return ''.join(s[:cursor])
