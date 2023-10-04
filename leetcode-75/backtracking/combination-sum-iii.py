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


class Solution2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(nums: List[int], count: int, target: int) -> List[List[int]]:
            if count == 0 and target == 0:
                return [[]]
            if not nums or count <= 0 or target <= 0:
                return []

            num, rest = nums[0], nums[1:]
            ans_with_num = dfs(rest, count - 1, target - num)
            for combination in ans_with_num:
                combination.append(num)
            ans_without_num = dfs(rest, count, target)
            return ans_with_num + ans_without_num

        return dfs(list(range(1, 10)), k, n)
