'''
Time: O(n^2)
Space: O(n^2)

n = numRows
'''

from typing import List

class Solution:
    def long_method(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for _ in range(1, numRows):
            item = [1]
            prev = res[-1]
            for i in range(len(prev) - 1):
                item.append(prev[i] + prev[i + 1])
            item.append(1)
            res.append(item)
        return res

    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for _ in range(1, numRows):
            prev = res[-1]
            res.append([1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1])
        return res
