'''
Time: O(n)
Space: O(1)

n = Length of array
'''

from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag_sq = 0
        area = 0

        for dimension in dimensions:
            l, w = dimension
            diag_sq = l * l + w * w  # Don't need to sqrt
        
            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                area = l * w
            elif diag_sq == max_diag_sq:
                area = max(area, l * w)
        return area
