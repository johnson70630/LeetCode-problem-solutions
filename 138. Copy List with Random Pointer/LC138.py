from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        new_node = Node(head.val)
        cur_new = new_node
        cur_old = head
        d = {}
        while cur_old.next is not None:
            node = Node(cur_old.next.val)
            cur_new.next = node
            d[cur_old] = cur_new
            cur_new = cur_new.next
            cur_old = cur_old.next
        d[cur_old] = cur_new

        cur_new = new_node
        cur_old = head
        while cur_new is not None:
            if cur_old.random is not None:
                cur_new.random = d[cur_old.random]
            cur_new = cur_new.next
            cur_old = cur_old.next
        return new_node
