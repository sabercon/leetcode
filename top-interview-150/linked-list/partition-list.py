from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        front_head = front_tail = ListNode()
        back_head = back_tail = ListNode()
        while head:
            if head.val < x:
                front_tail.next = head
                front_tail = head
            else:
                back_tail.next = head
                back_tail = head
            head = head.next
        back_tail.next = None
        front_tail.next = back_head.next
        return front_head.next
