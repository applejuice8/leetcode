'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Length of array

=============== Algorithm ===============
1. Loop through each item
2. Check complement needed to add up to target
3. If complement seen before, return index of [complement, current]
4. Else, add to hash map
'''

def hash_map(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

'''
=============== Complexity ===============
Time:  O(n^2)
Space: O(n)

n = Length of array

=============== Algorithm ===============
1. Brute force each possible number pair
2. If both numbers add up to target and is not same, return index
'''
def brute_force(nums: list[int], target: int) -> list[int]:
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if num1 + num2 == target and i != j:
                return [i, j]
