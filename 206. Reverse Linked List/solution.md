## LeetCode 206. Reverse Linked List

### Solution 1:
1. Loop over the original linked list, using a list to store each ListNode.
2. Create a dummy node, then loop over the stored nodes list in reverse order and link them sequentially.
3. Connect the last node to None to prevent the linked list from becoming cyclic.

### Solution 2:
1. Create two pointers, one pointing to None and the other to the head.
2. Loop over the original linked list. First, store the next node of `cur`, then link `cur` to `prev`. Continue this until `cur` is None, completing the reversal! (Storing `cur.next` is necessary because linking `cur` to `prev` changes the next pointer, making it impossible to move to the next node otherwise.)