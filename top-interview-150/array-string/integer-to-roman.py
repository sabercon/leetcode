class Solution:
    def intToRoman(self, num: int) -> str:
        roman = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
                 (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'),
                 (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        ans = ''
        while num > 0:
            while roman[-1][0] > num:
                roman.pop()
            num -= roman[-1][0]
            ans += roman[-1][1]
        return ans


class Solution2:
    def intToRoman(self, num: int) -> str:
        ones = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
        tens = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
        huns = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
        thos = ('', 'M', 'MM', 'MMM')
        return thos[num // 1000] + huns[num // 100 % 10] + tens[num // 10 % 10] + ones[num % 10]
