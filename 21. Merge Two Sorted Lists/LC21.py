from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur_d, cur1, cur2 = dummy, list1, list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur_d.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                cur_d.next = ListNode(cur2.val)
                cur2 = cur2.next
            cur_d = cur_d.next
        if cur1:
            cur_d.next = cur1
        elif cur2:
            cur_d.next = cur2
        return dummy.next
