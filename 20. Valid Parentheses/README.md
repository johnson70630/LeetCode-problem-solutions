## Leetcode 20. Valid Parentheses

### Solution:
1. Create a `dictionary` that maps closed parentheses (`keys`) to open parentheses (`values`).
2. Loop over the original string. Since open parentheses are values in the `dictionary`, use `in/not in` to determine if it's open or closed.
3. If it's not found, it means it's open, so append it to the stack. If found, it means it's closed, and you need to check if the last item in the stack corresponds to the matching open parenthesis (use the dictionary to find it).
4. If it matches, it means there's symmetry, so pop the last item from the stack. If it doesn't match, return `False`.
5. After the loop ends, check if the stack is empty. If it is, return `True`.