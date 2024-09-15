## LeetCode 148. Sort List

### Solution:
1. First, exclude empty Linked Lists and those with only one node.
2.	Use the merge sort method to find the middle of the Linked List, splitting it into two until the base case (a Linked List with just one node).
3.	To achieve the above, use a `getMid` function to find the midpoint (utilizing a `slow` and `fast` pointer—`slow` moves one step while `fast` moves two steps, so `slow` stops at the midpoint).
4.	After the `getMid` function returns, the `right` pointer will be at the midpoint. To split the list, create a `temp` node at the right’s next node, set right’s next node to `None`, and move the `right` pointer to `temp`, fully disconnecting the two Linked Lists.
5.	Use a recursive function to continue splitting both Linked Lists, reaching the base case as described in step 2.
6.	Reaching the base case means both sides are reduced to a single node, allowing the merge process to begin.
7.	For the logic behind the `merge` function, refer to [23. Merge k Sorted Lists](../23.%20Merge%20k%20Sorted%20Lists/)