'''
Time: O(n)
Space: O(1)

n = Length of array
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:  # type: ignore
        res = 0

        for num in nums:
            if num != val:
                nums[res] = num
                res += 1
        return res