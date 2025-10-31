'''
Time: O(n * d)
Space: O(1)

n = Length of array
d = Maximum number of digits
'''

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            n = 0

            # Remove last digit, Count
            while num > 0:
                num //= 10
                n += 1

            # Check number of digits
            if n % 2 == 0:
                res += 1
        return res