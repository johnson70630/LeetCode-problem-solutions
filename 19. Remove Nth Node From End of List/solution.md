## LeetCode 19. Remove Nth Node From End of List

### Solution:

1. Loop over `ListNode`, use a list to store each node.
2. Use list length - n to find the nth node from the end, and link the node before this node to the next node of this node.
3. Exclude cases that would cause out of range errors in the list:
    - Only one node
    - The node to be removed is the last node
    - The node to be removed is the first node