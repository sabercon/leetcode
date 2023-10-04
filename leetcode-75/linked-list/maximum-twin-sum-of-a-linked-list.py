from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next

        reversed_node = slow.next
        reversed_head = None
        while reversed_node:
            node = reversed_node
            reversed_node = node.next
            node.next = reversed_head
            reversed_head = node

        ans = 0
        while reversed_head:
            ans = max(ans, head.val + reversed_head.val)
            head = head.next
            reversed_head = reversed_head.next
        return ans
