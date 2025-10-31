'''
Time: O(n)
Space: O(1)

n = Length of array
'''

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0

        for num in nums:
            if num != val:
                nums[res] = num
                res += 1
        return res