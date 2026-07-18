'''
=============== Complexity ===============
Time:  O(n + log m)
Space: O(1)

n = Length of nums
m = min(nums)

=============== Algorithm ===============
1. Use math.gcd (Euclidean algorithm)
'''
import math

def euclidean(nums: list[int]) -> int:
    return math.gcd(min(nums), max(nums))


'''
=============== Complexity ===============
Time:  O(n + log m)
Space: O(1)

n = Length of nums
m = min(nums)

=============== Algorithm ===============
1. Find min, max of nums
2. Repeatedly apply a, b = b, a % b until b == 0
3. Return a as GCD
'''
def manual_euclidean(nums: list[int]) -> int:
    a, b = max(nums), min(nums)
    while b:
        a, b = b, a % b
    return a


'''
=============== Complexity ===============
Time:  O(n + m)
Space: O(1)

n = Length of nums
m = min(nums)

=============== Algorithm ===============
1. Find min and max of nums
2. Iterate downward from min, return first common divisor
'''
def brute_force(nums: list[int]) -> int:
    mini, maxi = min(nums), max(nums)
    
    # Iterate from top, return first match
    for i in range(mini, 0, -1):
        if maxi % i == 0 and mini % i == 0:
            return i
    return 1
