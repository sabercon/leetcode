from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy = odd = ListNode()
        even_dummy = even = ListNode()
        while head:
            odd.next = head
            odd = odd.next
            even.next = head.next
            even = even.next
            head = head.next.next if head.next else None
        odd.next = even_dummy.next
        return odd_dummy.next
