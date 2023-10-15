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
