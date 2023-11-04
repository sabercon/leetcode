from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        nodes = [root] if root else []
        while nodes:
            ans.append([node.val for node in nodes])
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
        return ans
