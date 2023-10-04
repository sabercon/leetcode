class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin(c & ~(a | b)).count("1") + bin(~c & a).count("1") + bin(~c & b).count("1")
