LeetCode 104. Maximum Depth of Binary Tree

Solution:

1. Pass the root and depth into the helper function.
2. The base case for the recursion is when the node is null, at which point the current depth is returned.
3. Use recursion to continuously explore the depths of the left and right subtrees, incrementing the depth by 1 each time until reaching the base case. Finally, return the greater depth.