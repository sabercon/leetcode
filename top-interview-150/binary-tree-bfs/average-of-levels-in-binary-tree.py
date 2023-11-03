from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        nodes = [root]
        while nodes:
            ans.append(sum(node.val for node in nodes) / len(nodes))
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
        return ans
