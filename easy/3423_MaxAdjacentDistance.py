'''
Time: O(n)
Space: O(1)

n = Length of array
'''

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:      # type: ignore
        max_diff = 0

        # First iteration is 0, -1
        for i in range(len(nums)):
            diff = abs(nums[i] - nums[i - 1])
            max_diff = max(diff, max_diff)
        return max_diff
