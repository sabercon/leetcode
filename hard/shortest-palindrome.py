class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        This problem is hard. The KMP solution is also worth exploring.
        """

        def palindrome_size(n: int) -> int:
            i = 0
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    i += 1
            return n if i == n else palindrome_size(i)

        return s[palindrome_size(len(s)):][::-1] + s
