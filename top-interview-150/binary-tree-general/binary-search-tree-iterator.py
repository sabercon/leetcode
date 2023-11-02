from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_back(root)

    def next(self) -> int:
        node = self.stack.pop()
        self._push_back(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _push_back(self, node: Optional[TreeNode]) -> None:
        if node:
            self.stack.append(node)
            self._push_back(node.left)
