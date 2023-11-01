from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(next=head)
        while node.next and node.next.next:
            if node.next.val != node.next.next.val:
                node = node.next
            else:
                duplicated = node.next.val
                while node.next and node.next.val == duplicated:
                    node.next = node.next.next
        return dummy.next
