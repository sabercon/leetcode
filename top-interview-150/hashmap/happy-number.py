class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return False
            seen.add(n)
        return True


class Solution2:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares_of_digits(n: int) -> int:
            return sum(int(i) ** 2 for i in str(n))

        slow = n
        fast = sum_of_squares_of_digits(n)
        while slow != fast and fast != 1:
            slow = sum_of_squares_of_digits(slow)
            fast = sum_of_squares_of_digits(sum_of_squares_of_digits(fast))
        return fast == 1
