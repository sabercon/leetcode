from itertools import zip_longest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafs(root):
            if root:
                yield from leafs(root.left)
                yield from leafs(root.right)
                if not root.left and not root.right:
                    yield root.val

        return all(leaf1 == leaf2 for leaf1, leaf2 in zip_longest(leafs(root1), leafs(root2)))
