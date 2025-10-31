'''
Time: O(d)
Space: O(d)

d = Number of digits
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))

        # Change first 6 to 9
        for i, digit in enumerate(s):
            if digit == '6':
                s[i] = '9'
                return int(''.join(s))
        
        # It's already biggest
        return num
