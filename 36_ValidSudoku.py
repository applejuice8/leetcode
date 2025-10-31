'''
Time: O(n^2)
Space: O(1)

n = Length of array
'''

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        cube = [set() for _ in range(size)]

        for i in range(size):
            row = set()
            col = set()

            for j in range(size):
                cube_index = (i // 3) * 3 + (j // 3)

                # Check row and cube
                item = board[i][j]
                if item != '.':
                    if item in row or item in cube[cube_index]:
                        return False
                    row.add(item)
                    cube[cube_index].add(item)

                # Check col
                item = board[j][i]
                if item != '.':
                    if item in col:
                        return False
                    col.add(item)
        return True
