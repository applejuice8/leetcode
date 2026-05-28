'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Length of str

=============== Algorithm ===============
1. Strip whitespace on right
2. Split at space
3. Get length of last element
'''
def strip_split(s: str) -> int:
    return len(s.rstrip().split()[-1])

'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of str

=============== Algorithm ===============
1. Loop from behind
2. Stop when encounter space
'''
def reverse_loop(s: str) -> int:
    s = s.rstrip()
    res = 0

    # Start from behind, break when space
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            break
        res += 1
    return res
