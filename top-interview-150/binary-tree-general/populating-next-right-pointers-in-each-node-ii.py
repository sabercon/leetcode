# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Builds the next pointer for the right child first, then the left child.
        """

        def do_connect(node: Node | None) -> None:
            if not node:
                return
            if node.left and node.right:
                node.left.next = node.right
                node.right.next = find_next(node.next)
            elif node.left:
                node.left.next = find_next(node.next)
            elif node.right:
                node.right.next = find_next(node.next)
            do_connect(node.right)
            do_connect(node.left)

        def find_next(parent: Node | None) -> Node | None:
            if not parent:
                return None
            if parent.left:
                return parent.left
            if parent.right:
                return parent.right
            return find_next(parent.next)

        do_connect(root)
        return root
