'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Number of digits

=============== Algorithm ===============
1. Change first 6 to 9
'''

def str_replace(num: int) -> int:
    return int(str(num).replace('6', '9', 1))

def list_replace(num: int) -> int:
    s = list(str(num))

    # Change first 6 to 9
    for i, digit in enumerate(s):
        if digit == '6':
            s[i] = '9'
            return int(''.join(s))
    return num
