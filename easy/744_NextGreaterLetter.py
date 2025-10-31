'''
Time: O(log n)
Space: O(1)

n = Length of array
'''

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        res = letters[0]

        while low <= high:
            mid = (low + high) // 2
            l = letters[mid]

            if l <= target:
                low = mid + 1
            elif l > target:
                high = mid - 1
                res = l
        return res
