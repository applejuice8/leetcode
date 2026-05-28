'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
1. 2 pointers num (Fast pointer), res (Slow pointer)
2. Iterate array with fast pointer
3. Increment res only if num wanted
4. If num wanted, overwrite array item at index res
5. Unwanted num are ignored, overwritten by wanted num
6. Current insert index is number of wanted num
'''

def two_pointers(nums: list[int], val: int) -> int:
    res = 0

    for num in nums:
        # Add to list if wanted
        if num != val:
            nums[res] = num
            res += 1
    return res
