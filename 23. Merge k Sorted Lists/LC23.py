from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        head1 = lists[0]
        for i in range(1, len(lists)):
            head2 = lists[i]
            head1 = self.merge(head1, head2)
        return head1
    
    def merge(self, head1, head2):
        dummy = cur = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next