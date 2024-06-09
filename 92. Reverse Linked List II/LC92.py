from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        left_node = ListNode(next=head)
        for _ in range(left - 1):
            left_node = left_node.next
        right_node = left_node.next

        prev, cur = right_node, right_node.next
        for _ in range(right - left):
            cur_next = cur.next
            cur.next = prev
            prev, cur = cur, cur_next
        if left == 1:
            head = prev
        right_node.next = cur
        left_node.next = prev
        return head
