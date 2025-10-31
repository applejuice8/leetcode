'''
Time: O(n)
Space: O(1)

Time: O(log n)
Space: O(1)

n = Length of array
'''

from typing import List

class Solution:
    def count(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        return max(pos, neg)

    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # Binary search
        # Count pos
        low = 0
        high = n - 1
        first_pos = n   # If none

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > 0:
                first_pos = mid
                high = mid - 1
            else:
                low = mid + 1
        
        # Count neg
        low = 0
        high = n - 1
        first_non_neg = n   # If none

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= 0:
                first_non_neg = mid
                high = mid - 1
            else:
                low = mid + 1
        return max(n - first_pos, first_non_neg)