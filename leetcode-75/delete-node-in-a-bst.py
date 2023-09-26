from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def pop_max(node: TreeNode) -> Tuple[int, Optional[TreeNode]]:
            if not node.right:
                return node.val, node.left
            max_val, node.right = pop_max(node.right)
            return max_val, node

        if not root:
            return None
        if key == root.val:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            root.val, root.left = pop_max(root.left)
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
