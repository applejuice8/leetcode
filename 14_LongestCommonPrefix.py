'''
Time: O(n * m)
Space: O(1)

n = Length of array
m = Length of shortest str
'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        # Length of shortest str
        for i in range(min(len(s) for s in strs)):
            c = strs[0][i]

            # Only append to res if in all strs
            for s in strs:
                if s[i] != c:
                    return res
            res += c
        return res
