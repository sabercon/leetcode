from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: TreeNode, i: int) -> (int | None, int):
            if not node:
                return None, i
            found, i = dfs(node.left, i)
            if found is not None:
                return found, 0
            if i == 1:
                return node.val, 0
            return dfs(node.right, i - 1)

        return dfs(root, k)[0]
