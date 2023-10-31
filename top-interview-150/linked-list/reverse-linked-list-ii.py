from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        start = dummy
        for _ in range(1, left):
            start = start.next

        end = start.next
        for _ in range(left, right):
            temp = end.next
            end.next = end.next.next
            temp.next = start.next
            start.next = temp

        return dummy.next
