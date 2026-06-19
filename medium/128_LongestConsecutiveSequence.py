'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Length of array

=============== Algorithm ===============
1. Set to remove duplicates
2. Find start of sequence (When the smaller number doesn't exist)
3. Count the sequence by iterating its increments
4. Keep track of the longest
'''

def iterate_set(nums: list[int]) -> int:
    res = 0  # Empty list
    num_set = set(nums)

    for num in num_set:
        # Start of sequence
        if (num - 1) not in num_set:
            length = 1

            # Accumulate subsequent elements
            while (num + length) in num_set:
                length += 1
            res = max(res, length)
    return res
