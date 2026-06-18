'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Length of array

=============== Algorithm ===============
1. Initiate a hash map, a list of buckets
2. Count each num frequency
3. Add each count to their respective bucket
4. Iterate from highest freq, add to res until enough k elements
'''

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]

    # Count
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # Add num to their respective bucket
    for key, c in count.items():
        freq[c].append(key)
    
    # Iterate from top
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for f in freq[i]:
            res.append(f)
            if len(res) == k:
                return res
