from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for str in strs:
            word = ''.join(sorted(str))
            d[word].append(str)
        return list(d.values())
