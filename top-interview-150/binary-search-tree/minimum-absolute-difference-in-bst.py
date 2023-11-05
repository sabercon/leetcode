from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> (int, int, int):
            min_val = max_val = node.val
            min_diff = float('inf')
            if node.left:
                left_min, left_max, left_diff = dfs(node.left)
                min_val = left_min
                min_diff = min(min_diff, left_diff, node.val - left_max)
            if node.right:
                right_min, right_max, right_diff = dfs(node.right)
                max_val = right_max
                min_diff = min(min_diff, right_diff, right_min - node.val)
            return min_val, max_val, min_diff

        return dfs(root)[2]
