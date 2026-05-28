'''
=============== Complexity ===============
Time:  O(m + n)
Space: O(1)

m = Length of s
n = Length of t

=============== Algorithm ===============
1. If different length cannot be anagrams
2. Use hash map store count of each letter for each
3. Anagram if both hash map equal
'''

def hash_map(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1
    return count_s == count_t
