from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] + 1:
                ans[-1] = ans[-1].split('->')[0] + '->' + str(nums[i])
            else:
                ans.append(str(nums[i]))
        return ans
