from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def do_flatten(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            left_first, right_first = node.left, node.right
            left_last, right_last = do_flatten(node.left), do_flatten(node.right)
            if left_first:
                node.left = None
                node.right = left_first
                left_last.right = right_first
            return right_last or left_last or node

        do_flatten(root)


class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        last, current = TreeNode(), root
        while current:
            left, right = current.left, current.right
            current.left = current.right = None
            last.right = current
            last = current

            if left:
                left_last = left
                while left_last.right:
                    left_last = left_last.right
                left_last.right = right

                current = left
            else:
                current = right
        return root
