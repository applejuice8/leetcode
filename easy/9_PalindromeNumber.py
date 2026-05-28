'''
=============== Complexity ===============
Time:  O(log n)
Space: O(1)

n = Length of n

=============== Algorithm ===============
1. Return true if 0
2. Return false if negative or end with 0
3. Remove numbers on right half until >= numbers on left half
4. Remove last digit of right half if odd
5. Compare left, right
'''
def compare_left_right(x: int) -> bool:
    # 0 is palindrome
    if x == 0:
        return True

    # All negatives not palindrome
    # All num end with 0 not palindrome
    if x < 0 or x % 10 == 0:
        return False

    rev = 0
    while x > rev:
        digit = x % 10  # Get last digit
        x //= 10    # Remove last digit
        rev = rev * 10 + digit  # Move all digits 1 place left, add new digit
    
    # For odd length, rev extra 1 digit (The middle digit)
    return x == rev or x == rev // 10

'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Number of digits

=============== Algorithm ===============
1. Convert int to str
2. Use 2 pointers (1 front, 1 back)
3. Return false if 2 pointers different
'''
def convert_to_str(x: int) -> bool:
    s = str(x)
    length = len(s)

    # 2 pointers (1 from front, 1 from back)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True
