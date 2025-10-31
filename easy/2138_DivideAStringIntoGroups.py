'''
Time: O(n)
Space: O(n)

n = Length of s
'''

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        group = []
        word = ''

        # Append when long enough
        for char in s:
            word += char
            if len(word) == k:
                group.append(word)
                word = ''
        
        # Fill empty
        if word:
            word += fill * (k - len(word))
            group.append(word)
        return group
