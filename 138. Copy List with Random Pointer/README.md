## LeetCode 138. Copy List with Random Pointer

### Solution:
1. Loop over the `original Node (head)`. In each iteration, create a `new Node` and connect it to the `new ListNode`.
2. Since the `random pointer` of the `new ListNode` might not have been created yet during the first loop, use a `dictionary` to store the mapping between the `old Node` and the `new Node`.
3. Finally, loop over the `new ListNode` again to assign the corresponding `random pointers`.