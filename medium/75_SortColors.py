'''
Time: O(n)
Space: O(1)

n = Length of array
'''

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        # Dutch National Flag Algorithm
        # 3 pointers, mid iterate, if low/high then add to low/high, else dont touch
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1
