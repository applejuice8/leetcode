'''
Time: O(n)
Space: O(n)
n = Number of digits

Time: O(log n)
Space: O(1)
n = The int itself
'''

class Solution:
    def convert_to_str(self, x: int) -> bool:
        x = str(x)

        # 2 pointers (1 from front, 1 from back)
        for i in range(len(x) // 2):
            if x[i] != x[len(x) - 1 - i]:
                return False
        return True

    def isPalindrome(self, x: int) -> bool:
        # All negatives not palindrome
        if x < 0:
            return False

        # All num end with 0 not palindrome (Because num cannot first)
        if x != 0 and x % 10 == 0:
            return False

        rev = 0
        while x > rev:
            digit = x % 10  # Get last digit
            rev = rev * 10 + digit
            x //= 10    # Remove last digit
        
        # For odd length, rev extra 1 digit (The middle digit)
        return x == rev or x == rev // 10
