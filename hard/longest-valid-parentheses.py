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
