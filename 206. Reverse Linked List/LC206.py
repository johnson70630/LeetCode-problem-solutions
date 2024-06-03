from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original = []
        cur = head
        while cur is not None:
            original.append(cur)
            cur = cur.next
        dummy = ListNode()
        cur = dummy
        for node in reversed(original):
            cur.next = node
            cur = cur.next
        cur.next = None
        return dummy.next


    def reverseList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev, cur = cur, cur_next
        return prev
