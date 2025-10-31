'''
Time: O(n)
Space: O(1)

n = Length of s
'''

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = {}
        con = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for c in s:
            if c in vowels:
                vow[c] = vow.get(c, 0) + 1
            else:
                con[c] = con.get(c, 0) + 1
        
        max_vow = max(vow.values()) if vow else 0
        max_con = max(con.values()) if con else 0

        return max_vow + max_con
