from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Definitely not an easy problem.
        """

        if str1 + str2 != str2 + str1:
            return ''
        return str1[:gcd(len(str1), len(str2))]
