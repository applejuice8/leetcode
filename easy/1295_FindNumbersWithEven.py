'''
=============== Complexity ===============
Time:  O(n * d)
Space: O(1)

n = Length of array
d = Maximum number of digits

=============== Algorithm ===============
1. For each num, count digit using floor operator
2. Check if n is even
'''

def floor(nums: list[int]) -> int:
    res = 0

    for num in nums:
        n = 0

        # Remove last digit, Count
        while num > 0:
            num //= 10
            n += 1

        # Count number of digits
        if n % 2 == 0:
            res += 1
    return res
