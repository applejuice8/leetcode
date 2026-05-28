'''
=============== Complexity ===============
Time:  O(n^2)
Space: O(n^2)

n = numRows

=============== Algorithm ===============
1. Start with first row
2. For each row, add 1 as first element
3. Append addition result of 2 cell above
4. For each row, add 1 as last element
'''

def long_method(numRows: int) -> list[list[int]]:
    res = [[1]]

    for _ in range(1, numRows):
        item = [1]

        prev = res[-1]
        for i in range(len(prev) - 1):
            item.append(prev[i] + prev[i + 1])

        item.append(1)
        res.append(item)
    return res

def list_comprehension(numRows: int) -> list[list[int]]:
    res = [[1]]

    for _ in range(1, numRows):
        prev = res[-1]
        res.append([1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1])
    return res
