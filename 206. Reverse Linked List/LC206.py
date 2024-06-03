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
            original.append(cur.val)
            cur = cur.next
        dummy = ListNode()
        cur = dummy
        for num in reversed(original):
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next


    def reverseList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            dummy = ListNode(next=head)
            back, middle, front = dummy, head, head.next
            while front:
                back, middle, front = middle, front, front.next
                middle.next = back
            head.next = None
            return middle
        return head