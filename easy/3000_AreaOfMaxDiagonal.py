'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of array

=============== Algorithm ===============
1. Iterate each dimension
2. If diag_sq largest, store the area
3. If multiple diag_sq largest, return max area
'''

def area_of_max_diagonal(dimensions: list[list[int]]) -> int:
    max_diag_sq = area = 0

    for dimension in dimensions:
        l, w = dimension
        diag_sq = l * l + w * w

        if diag_sq > max_diag_sq:
            max_diag_sq = diag_sq
            area = l * w
        elif diag_sq == max_diag_sq:
            area = max(area, l * w)
    return area
