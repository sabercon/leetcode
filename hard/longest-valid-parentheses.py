class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        start = -1
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif not stack:
                start = i
            else:
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else start))
        return ans


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, l + r)
            if l < r:
                l = r = 0

        l = r = 0
        for c in reversed(s):
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ans = max(ans, l + r)
            if l > r:
                l = r = 0
        return ans
