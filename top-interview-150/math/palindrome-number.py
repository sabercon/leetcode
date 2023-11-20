class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_x = x
        reversed_x = 0
        while x > 0:
            x, r = divmod(x, 10)
            reversed_x = reversed_x * 10 + r
        return original_x == reversed_x
