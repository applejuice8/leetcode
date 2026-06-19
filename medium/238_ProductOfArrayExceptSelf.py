'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of nums

=============== Algorithm ===============
1. Instead of recalculating every time, store product of left and right (prefix, suffix)
2. res[i] = left[i] * right[i]
'''

def prefix_suffix(nums: list[int]) -> list[int]:
    n = len(nums)

    left = [0] * n
    right = [0] * n
    res = [0] * n

    left[0] = right[n - 1] = 1

    for i in range(1, n):
        # Left of index 5 is index 4 * left of index 4
        left[i] = nums[i - 1] * left[i - 1]
    for i in range(n - 2, -1, -1):
        # Right of index 5 is index 6 * right of index 6
        right[i] = nums[i + 1] * right[i + 1]
    
    for i in range(n):
        res[i] = left[i] * right[i]
    return res
