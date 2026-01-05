'''
Time: O(n)
Space: O(n)

n = Length of array
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:   # type: ignore
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
