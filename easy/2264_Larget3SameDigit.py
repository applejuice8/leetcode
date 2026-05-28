'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of num

=============== Algorithm ===============
1. Iterate num
2. Find substring with 3 same num
3. Get max between current 3 and prev 3
'''

def largestGoodInteger(num: str) -> str:
    res = ''

    for i in range(len(num) - 2):
        if num[i] == num[i + 1] == num[i + 2]:
            res = max(res, num[i] * 3)
    return res
