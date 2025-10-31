'''
Time: O(d)
Space: O(d)

d = Number of digits
'''

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        n_max = num # If all 9

        # Max (Replace first non-9 to 9)
        for char in s:
            if char != '9':
                n_max = int(s.replace(char, '9'))
                break

        # Min (Replace all occurence of first digit with 0)
        n_min = int(s.replace(s[0], '0'))

        return n_max - n_min