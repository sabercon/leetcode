from itertools import groupby
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return [list(group) for _, group in groupby(sorted(strs, key=sorted), key=sorted)]
