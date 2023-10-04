from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zig_zag(node: Optional[TreeNode], direction: str, length: int) -> int:
            if not node:
                return length
            if direction == 'left':
                return max(zig_zag(node.left, 'right', length + 1), zig_zag(node.right, 'left', 1))
            if direction == 'right':
                return max(zig_zag(node.right, 'left', length + 1), zig_zag(node.left, 'right', 1))

        return zig_zag(root, 'left', 0) - 1
