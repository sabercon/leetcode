from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if not node:
                return 0, -1000
            max_sum_from_left, max_sum_in_left = dfs(node.left)
            max_sum_from_right, max_sum_in_right = dfs(node.right)
            max_sum_from_node = max(node.val + max(max_sum_from_left, max_sum_from_right), 0)
            max_sum = max(max_sum_in_left, max_sum_in_right, node.val + max_sum_from_left + max_sum_from_right)
            return max_sum_from_node, max_sum

        return dfs(root)[1]
