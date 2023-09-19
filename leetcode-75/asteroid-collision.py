from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                last = stack[-1]
                if last <= -a:
                    stack.pop()
                if last >= -a:
                    break
            else:
                stack.append(a)
        return stack
