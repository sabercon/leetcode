from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        start = dummy
        while start.next:
            temp = start
            for _ in range(k):
                temp = temp.next
                if not temp:
                    return dummy.next

            end = start.next
            for _ in range(k - 1):
                temp = end.next
                end.next = temp.next
                temp.next = start.next
                start.next = temp
            start = end
        return dummy.next
