'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
1. Iterate nums
2. Count pos, neg
3. Get max of pos, neg
'''

def count(nums: list[int]) -> int:
    pos = neg = 0

    for num in nums:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
    return max(pos, neg)


'''
=============== Complexity ===============
Time:  O(log n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
1. Binary search get index of first zero / pos
2. Index of first zero / pos is len of neg
3. Skip zeros for first_non_neg
4. Len of pos is len(nums) - first_non_neg
'''

def binary_search(nums: list[int]) -> int:
    n = len(nums)
    low, high = 0, n - 1
    first_non_neg = n

    # Get index of first zero / pos
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= 0:
            first_non_neg = mid
            high = mid - 1
        else:
            low = mid + 1
    
    # Skip all zeros
    first_pos = first_non_neg
    while first_pos < n and nums[first_pos] == 0:
        first_pos += 1

    return max(first_non_neg, n - first_pos)
