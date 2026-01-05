'''
Time: O(n)
Space: O(n)

n = Length of nums
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   # type: ignore
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Count
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Add num to their respective count bucket
        for key, c in count.items():
            freq[c].append(key)
        
        # Iterate from top
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
