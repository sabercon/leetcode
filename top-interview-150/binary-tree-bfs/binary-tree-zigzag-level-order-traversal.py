from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        nodes = [root] if root else []
        left_to_right = True
        while nodes:
            ans.append([node.val for node in (nodes if left_to_right else reversed(nodes))])
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
            left_to_right = not left_to_right
        return ans
