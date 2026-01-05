'''
Time: O(n)
Space: O(1)

n = Length of bits
'''

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:   # type: ignore
        i = 0
        n = len(bits) - 1

        while i <= n:
            bit = bits[i]
            i += 2 if bit else 1
        return False if bit else True
