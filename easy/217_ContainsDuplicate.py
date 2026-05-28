'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Length of nums

=============== Algorithm ===============
1. Use set store seen elements
'''

def use_set(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
