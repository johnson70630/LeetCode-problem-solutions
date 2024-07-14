## LeetCode 49. Group Anagrams

### Solution:
1. Loop over the `list` of words and extract each word.
2. Use `sorted` to sort the letters of the word into a list, and use `join` to convert it back to a string.
3. Store the sorted string in a `dictionary` as the `key`, with the value being a `list` of words that match the sorted letters. This groups all words with the same letters together in one list.
4. Finally, collect all the value lists from the `dictionary`.