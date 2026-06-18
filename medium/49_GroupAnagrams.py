'''
=============== Complexity ===============
Time:  O(m * n)
Space: O(m * n)

m = Number of strs
n = Average length of each string

=============== Algorithm ===============
1. Itearate each str
2. For each str, initialize empty list of 26 elements, 1 for each alphabet
3. Count frequency of each char
4. Store counts in hash map using tuple of the list of 26 elements
'''

def list_of_26_alphabet_counts(strs: list[str]) -> list[list[str]]:
    res = {}  # Or collections.defaultdict(list)
    base = ord('a')

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - base] += 1
        res.setdefault(tuple(count), []).append(s)
    return list(res.values())

'''
=============== Complexity ===============
Time:  O(m * nlogn)
Space: O(m * n)

m = Number of strs
n = Average length of each string

=============== Algorithm ===============
1. Itearate each str
2. For each str, use sorted str as key to append into hash map
'''

def use_sorted_str_as_key(strs: list[str]) -> list[list[str]]:
    res = {}

    for s in strs:
        key = ''.join(sorted(s))
        res.setdefault(key, []).append(s)
    return list(res.values())

in_val = ["eat","tea","tan","ate","nat","bat"]
out_val = [["bat"],["nat","tan"],["ate","eat","tea"]]
ans1 = list_of_26_alphabet_counts(in_val)
ans2 = use_sorted_str_as_key(in_val)
assert sorted([sorted(a) for a in ans1]) == sorted([sorted(b) for b in out_val])
assert sorted([sorted(a) for a in ans2]) == sorted([sorted(b) for b in out_val])
