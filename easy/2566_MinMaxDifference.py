'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Number of digits

=============== Algorithm ===============
1. For max, replace first non-9 with 9
2. For min, replace first digit with 0
3. Return max - min
'''

def replace_first_digit(num: int) -> int:
    n_max = num  # If all 9
    s = str(num)

    # Max (Replace first non-9 with 9)
    for char in s:
        if char != '9':
            n_max = int(s.replace(char, '9'))
            break

    # Min (Replace first digit with 0)
    n_min = int(s.replace(s[0], '0'))

    return n_max - n_min
