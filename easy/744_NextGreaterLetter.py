'''
=============== Complexity ===============
Time:  O(log n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
1. Use binary search
2. Start with first element (Fallback if no answer)
3. If letter bigger than target, continue to find smaller answer (If got)
4. If letter smaller than targer, search the bigger half
'''

def binary_search(letters: list[str], target: str) -> str:
    low, high = 0, len(letters) - 1
    res = letters[0]

    while low <= high:
        mid = (low + high) // 2
        l = letters[mid]

        if l <= target:
            low = mid + 1
        elif l > target:
            high = mid - 1
            res = l
    return res
