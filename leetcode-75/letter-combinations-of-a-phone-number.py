from typing import List


class Solution:
    def __init__(self):
        self.mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = self.letterCombinations(digits[1:]) or ['']
        return [letter + combination for letter in self.mapping[digits[0]] for combination in combinations]
