'''
=============== Complexity ===============
Time:  O(log n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
Binary search
'''

def binary_search(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    # Classic binary search
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
