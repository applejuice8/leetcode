'''
Time: O(m * n)
Space: O(m * n)

m = Length of strs
n = Average length of each string
'''

'''
Notes
- defaultdict(list) is a dict that auto creates list when access invalid index KeyError
- Store a list containing frequency of 26 chars
- Convert the list to tuple to use as index for dict
- Convert defaultdict to list before return
'''

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        base = ord('a')

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - base] += 1
            res[tuple(count)].append(s)
        return list(res.values())
