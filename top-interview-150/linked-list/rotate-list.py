from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head
        size = 1
        while tail.next:
            tail = tail.next
            size += 1
        tail.next = head

        for _ in range(size - k % size - 1):
            head = head.next
        ans = head.next
        head.next = None
        return ans
