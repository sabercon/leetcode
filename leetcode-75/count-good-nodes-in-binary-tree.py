# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good_nodes(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            if node.val >= max_val:
                return 1 + good_nodes(node.left, node.val) + good_nodes(node.right, node.val)
            else:
                return good_nodes(node.left, max_val) + good_nodes(node.right, max_val)

        return good_nodes(root, root.val)
