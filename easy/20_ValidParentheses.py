'''
Time: O(n)
Space: O(n)

n = Length of s
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for brac in s:
            if brac in brac_pairs:  # Close brac
                if stack and stack[-1] == brac_pairs[brac]:
                    stack.pop()
                else:
                    return False
            else:   # Open brac
                stack.append(brac)
        return True if not stack else False
