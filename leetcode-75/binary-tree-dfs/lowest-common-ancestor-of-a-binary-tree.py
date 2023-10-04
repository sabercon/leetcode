from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: Optional[TreeNode]) -> Tuple[bool, Optional[TreeNode]]:
            if not node:
                return False, None

            left_lca, left = dfs(node.left)
            if left_lca:
                return True, left

            right_lca, right = dfs(node.right)
            if right_lca:
                return True, right

            nodes = (node, left, right)
            found = [n for n in (p, q) if n in nodes]
            if len(found) > 1:
                return True, node
            return False, found[0] if found else None

        return dfs(root)[1]
