from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur, passed = head, []
        while cur is not None:
            if cur in passed:
                return True
            passed.append(cur)
            cur = cur.next
        return False
