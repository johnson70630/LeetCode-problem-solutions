## LeetCode 15. 3Sum

### Solution:
1. First, sort the list of numbers.
2. Loop over each number, and for each number, calculate the difference from 0, which is the sum of the remaining two numbers `target`.
3. Use a two-pointer approach to find all possible pairs of numbers that sum up to the target:
   - Use `left` for the smaller number and `right` for the larger number.
   - If the total is too small, move `left` to the next number at right side.
   - If the total is too large, move `right` to the next number at left side.
   - When the target is found, move both pointers inward to find the next pair that meets the target sum.
4. To improve efficiency, skip over duplicate numbers in the loop to avoid redundant calculations. 