## LeetCode 125. Valid Palindrome

### Solution:
1. Remove all non-alphabet or number characters and convert to lowercase. (Initially, create a new string by looping over and appending only alphabet or number characters, but later found online that you can use join and write it in one line.)
2. Use a two-pointer approach to check if the characters from the beginning and end are the same. If not, return `False`. If all characters match, return `True`.