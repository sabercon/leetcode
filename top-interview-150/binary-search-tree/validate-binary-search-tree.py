from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, lower: int, upper: int) -> bool:
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, -2 ** 31 - 1, 2 ** 31)
