from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct_tree(x: int, y: int, length: int) -> Node:
            if length == 1:
                return Node(grid[x][y], True, None, None, None, None)
            half = length // 2
            tl = construct_tree(x, y, half)
            tr = construct_tree(x, y + half, half)
            bl = construct_tree(x + half, y, half)
            br = construct_tree(x + half, y + half, half)
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
                return Node(tl.val, True, None, None, None, None)
            else:
                return Node(0, False, tl, tr, bl, br)

        return construct_tree(0, 0, len(grid))
