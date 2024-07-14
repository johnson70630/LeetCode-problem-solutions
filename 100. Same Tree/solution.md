## LeetCode 100. Same Tree

### Solution:
1. Solve this problem using recursion with three base cases:
   1. When the same position in both `trees` is `null`, it means all previous `nodes` are the same. Return `True`. 
   2. When the same position in both `trees` has only one `null`, it means they are different `trees`. Return `False`. 
   3. When the values at the same position in both `trees` are different, it means they are different `trees`. Return `False`.
2. Continuously check the same positions in both `trees`. If they are the same, return `True`; if they are different, return `False`.






