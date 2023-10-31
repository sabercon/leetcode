from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Fantastic solution that associates the original node with its copy node in a single linked list.
        """

        temp = head
        while temp:
            copy = Node(temp.val, temp.next, temp.random)
            temp.next = copy
            temp = copy.next

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        temp = head
        dummy = copy_head = Node(0)
        while temp:
            copy_head.next = temp.next
            copy_head = copy_head.next
            temp.next = temp.next.next
            temp = temp.next
        return dummy.next
