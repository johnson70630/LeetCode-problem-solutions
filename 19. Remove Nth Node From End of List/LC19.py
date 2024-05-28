from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur is not None:
            nodes.append(cur)
            cur = cur.next
        if len(nodes) == 1:
            return None
        if n == 1:
            nodes[len(nodes)-2].next = None
        elif n == len(nodes):
            return head.next
        else:
            nodes[len(nodes)-n-1].next = nodes[len(nodes)-n+1]
        return head
