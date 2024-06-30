LeetCode 226. Invert Binary Tree

Solution:

1.	Use a recursion function with the base case being when the node is None, at which point you simply return the root. 
2.	As long as the root is not None, swap the left and right children, then recursively invert the left and right subtrees.