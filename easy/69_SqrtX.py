'''
Time: O(log x)
Space: O(1)

x = Input value
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        res = 0

        while low <= high:
            mid = (low + high) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res