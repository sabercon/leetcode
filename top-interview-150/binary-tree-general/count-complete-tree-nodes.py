from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_depth(node: Optional[TreeNode]) -> int:
            return 0 if not node else 1 + get_depth(node.left)

        def get_count(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return 0
            if get_depth(node.right) == depth - 1:
                return 2 ** (depth - 1) + get_count(node.right, depth - 1)
            else:
                return 2 ** (depth - 2) + get_count(node.left, depth - 1)

        return get_count(root, get_depth(root))
