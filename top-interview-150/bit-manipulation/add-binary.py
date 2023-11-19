from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        carry = 0
        for ac, bc in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            carry, bit = divmod(int(ac) + int(bc) + carry, 2)
            ans = str(bit) + ans
        return '1' + ans if carry else ans
