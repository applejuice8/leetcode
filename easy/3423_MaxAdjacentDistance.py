'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
1. Iterate each neighboring numbers
2. Start with 0, -1 (Since circular)
3. Store max_diff
'''

def maxAdjacentDistance(nums: list[int]) -> int:
    max_diff = 0

    # First iteration is 0, -1
    for i in range(len(nums)):
        diff = abs(nums[i] - nums[i - 1])
        max_diff = max(diff, max_diff)
    return max_diff
