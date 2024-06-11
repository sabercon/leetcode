from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if int(num) < abs(target):
            return []
        ans = []
        for i in range(len(num)):
            if i != len(num) - 1 and num[i] == '0':
                continue
            ans.extend(e + num[i:] for e in self.addOperatorsWithLast(num[:i], int(num[i:]), target))
        return ans

    def addOperatorsWithLast(self, num: str, last: int, target: int) -> List[str]:
        if not num:
            return [''] if last == target else []
        ans = []
        ans.extend(e + '+' for e in self.addOperators(num, target - last))
        ans.extend(e + '-' for e in self.addOperators(num, target + last))
        if (last != 0 and int(num) * last < abs(target)) or (last == 0 and int(num) < abs(target)):
            return ans
        for i in range(len(num)):
            if i != len(num) - 1 and num[i] == '0':
                continue
            ans.extend(e + num[i:] + '*' for e in self.addOperatorsWithLast(num[:i], int(num[i:]) * last, target))
        return ans
