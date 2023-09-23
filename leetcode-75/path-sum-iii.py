from collections import Counter
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Memorizes prefix sums to lower the time complexity to O(n).
        """

        pre_sums = Counter([0])

        def dfs(node: Optional[TreeNode], pre_sum: int) -> int:
            if not node:
                return 0
            cur_sum = pre_sum + node.val
            paths = pre_sums[cur_sum - targetSum]
            pre_sums[cur_sum] += 1
            paths += dfs(node.left, cur_sum) + dfs(node.right, cur_sum)
            pre_sums[cur_sum] -= 1
            return paths

        return dfs(root, 0)
