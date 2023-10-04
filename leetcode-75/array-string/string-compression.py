from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        size = 0
        i = 0
        while i < len(chars):
            char = chars[i]
            count = 1
            while i + 1 < len(chars) and char == chars[i + 1]:
                count += 1
                i += 1
            i += 1

            chars[size] = char
            size += 1
            if count != 1:
                count_str = str(count)
                chars[size: size + len(count_str)] = count_str
                size += len(count_str)

        return size
