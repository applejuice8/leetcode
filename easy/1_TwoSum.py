'''
Time: O(n)
Space: O(n)

n = Length of array
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    # type: ignore
        # Hash table store previously seen nums
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
