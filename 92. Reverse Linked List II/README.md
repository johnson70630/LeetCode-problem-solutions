## LeetCode 92. Reverse Linked List II

### Solution:
1. Create a `left_node` and traverse to the node just before the start of the reversal range. Exclude the nodes before the reversal range from being reversed.
2. `right_node` is the next node after `left_node` and will be used to connect to the remaining unreversed nodes.
3. Similar to the original reverse linked list problem, use two pointers to store the next node of `cur` and then reverse it, continuing until all nodes in the reversal range are reversed. At this point, `cur` will be on the node immediately after the reversal range.
4. Finally, connect `left_node` to the last node of the reversed range (`prev`), which after reversal is the first node of the range.
5. `right_node` was originally the first node of the reversal range and after reversal will be the last node, so it should be connected to the first node after the reversal range (`cur`).
6. If the first node is within the reversal range, `head` will be the last node of the reversal range before reversal (`prev`).