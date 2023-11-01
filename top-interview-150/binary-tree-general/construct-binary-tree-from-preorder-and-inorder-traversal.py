from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pre_start: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if in_start > in_end:
                return None
            root = TreeNode(preorder[pre_start])
            idx = inorder.index(preorder[pre_start], in_start, in_end + 1)
            root.left = build(pre_start + 1, in_start, idx - 1)
            root.right = build(pre_start + 1 + idx - in_start, idx + 1, in_end)
            return root

        return build(0, 0, len(inorder) - 1)


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = preorder[::-1]
        inorder = inorder[::-1]

        def build(parent: int | None) -> Optional[TreeNode]:
            if not inorder or inorder[-1] == parent:
                return None
            val = preorder.pop()
            root = TreeNode(val)
            root.left = build(val)
            inorder.pop()
            root.right = build(parent)
            return root

        return build(None)
