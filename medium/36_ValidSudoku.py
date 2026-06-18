'''
=============== Complexity ===============
Time:  O(1)
Space: O(1)

=============== Algorithm ===============
1. Initiate 9 empty sets (1 each for rows, cols, cubes)
2. Iterate each cell, Skip empty cells
3. If cell already in row / col / cube, return False
4. Else, add cell to row / col / cube
'''

def empty_sets(board: list[list[str]]) -> bool:
    SIZE = 9
    rows = [set() for _ in range(SIZE)]
    cols = [set() for _ in range(SIZE)]
    cubes = [set() for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            val = board[i][j]

            # Skip empty cells
            if val == '.':
                continue

            cube_index = (i // 3) * 3 + (j // 3)

            # If duplicate
            if val in rows[i] or val in cols[j] or val in cubes[cube_index]:
                return False

            rows[i].add(val)
            cols[j].add(val)
            cubes[cube_index].add(val)
    return True
