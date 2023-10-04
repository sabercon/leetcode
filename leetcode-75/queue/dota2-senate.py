from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = deque(), deque()
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))
        return 'Radiant' if radiant else 'Dire'
