'''
Time: O(n)
Space: O(n)

Time: O(n)
Space: O(1)

n = Length of s
'''

class Solution:
    def use_split(self, s: str) -> int:
        return len(s.rstrip().split()[-1])

    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        res = 0

        # Start from behind, break when space
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            res += 1
        return res