'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
1. Dutch national flag algorithm
2. 3 pointers, start from mid
3. If mid is low, swap mid with low, increment mid
4. If mid is high, swap mid with high, decrement high
5. If mid is mid, increment mid
'''

def sortColors(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
        else:
            mid += 1
