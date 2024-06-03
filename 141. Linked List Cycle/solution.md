## LeetCode 141. Linked List Cycle

### Solution:
1. Loop over the linked list and store each node in a list called `passed`.
2. If the last node points to one of the previous nodes in the `passed` list, it indicates that the linked list has a cycle.