class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = [0] * 26
        for c in magazine:
            i = ord(c) - ord('a')
            counter[i] += 1
        for c in ransomNote:
            i = ord(c) - ord('a')
            counter[i] -= 1
            if counter[i] < 0:
                return False
        return True
