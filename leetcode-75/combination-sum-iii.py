from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(nums: List[int], count: int, target: int, path: List[int]) -> None:
            if count == 0 and target == 0:
                ans.append(path)
                return
            if count <= 0 or target <= 0:
                return
            for i, num in enumerate(nums):
                dfs(nums[i + 1:], count - 1, target - num, path + [num])

        dfs(list(range(1, 10)), k, n, [])
        return ans
