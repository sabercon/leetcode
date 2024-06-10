class Solution:
    def numberToWords(self, num: int) -> str:
        words = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }
        if num in words:
            return words[num]
        for n, w in ((1_000_000_000, 'Billion'), (1_000_000, 'Million'), (1000, 'Thousand'), (100, 'Hundred')):
            if num >= n:
                return f'{self.numberToWords(num // n)} {w} {self.numberToWords(num % n)}'.removesuffix(' Zero')
        return self.numberToWords(num // 10 * 10) + ' ' + self.numberToWords(num % 10)
