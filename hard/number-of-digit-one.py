class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 10:
            return 1 if n > 0 else 0
        digits = str(n)
        first, rest = int(digits[0]), int(digits[1:])
        nines = (n - rest) // first - 1
        return self.countDigitOne(nines) * first + self.countDigitOne(rest) + 1 + (rest if first == 1 else nines)
