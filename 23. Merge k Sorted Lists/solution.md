## LeetCode 23. Merge k Sorted Lists

### Solution:
1.	Exclude empty `lists` first.
2.	Take the first two Linked Lists and assign a `head` to each, pointing to the first node of both Linked Lists.
3.	Create a `dummy node` and position `cur` at the `dummy node`.
4.	Compare the two `heads`; link the smaller value node to `cur`. Move both `cur` and the smaller node forward, repeating this process until one of the Linked Lists is fully traversed.
5.	Once one Linked List is exhausted, link `cur` to the remaining nodes of the other Linked List, and return the fully merged Linked List starting from the `dummy’s next node`.
6.	After merging, `head1` becomes the merged Linked List, and it is ready to be compared with the next Linked List. Repeat the process until all Linked Lists are merged.