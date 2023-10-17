from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line = []
        width = 0
        for word in words:
            if width + len(line) + len(word) > maxWidth:
                if len(line) > 1:
                    pack = ''
                    common_spaces = (maxWidth - width) // (len(line) - 1)
                    extra_spaces = (maxWidth - width) % (len(line) - 1)
                    for i, w in enumerate(line):
                        pack += w
                        if i < len(line) - 1:
                            pack += ' ' * (common_spaces + (1 if i < extra_spaces else 0))
                    ans.append(pack)
                else:
                    ans.append(line[0] + ' ' * (maxWidth - width))
                line = []
                width = 0
            line.append(word)
            width += len(word)
        ans.append(' '.join(line) + ' ' * (maxWidth - width - len(line) + 1))
        return ans
