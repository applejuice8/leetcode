'''
=============== Complexity ===============
Time:  O(log(n * m))
Space: O(1)

m = Number of rows
n = Number of cols

=============== Algorithm ===============
1. 2D binary search
2. Use floor operator for row
3. Use modulo operator for col
'''

def twoD_binary_search(matrix: list[list[int]], target: int) -> bool:
    h = len(matrix)
    w = len(matrix[0])

    low = 0
    high = h * w - 1

    while low <= high:
        mid = (low + high) // 2
        cell = matrix[mid // w][mid % w]
        
        if cell == target:
            return True
        elif cell < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
