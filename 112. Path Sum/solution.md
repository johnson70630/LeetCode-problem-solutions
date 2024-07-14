## LeetCode 112. Path Sum

### Solution:
1.	Use recursion until the encountered node is `None`, then return `False`.
2.	Track how much is left to reach the target sum from the current node (`need`).
3.	When both `left` and `right` children are `None`, it means we’ve reached a leaf node, and we can return `True` or `False`.
4.	If, upon reaching a leaf, the remaining target sum is `0`, return `True`; otherwise, return `False`.
5.	In the final step, continue exploring the `left` and `right` nodes. If either side meets the target sum, return `True`.