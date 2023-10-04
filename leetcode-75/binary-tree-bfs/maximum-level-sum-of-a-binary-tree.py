from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = 1
        max_sum = root.val
        current_level = 1
        queue = [root]

        while queue:
            current_sum = 0
            next_queue = []

            for node in queue:
                current_sum += node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                max_level = current_level

            current_level += 1
            queue = next_queue

        return max_level
