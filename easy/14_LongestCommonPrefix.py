'''
Better for long list (Bails out immediately if item1[0] != item2[0])

=============== Complexity ===============
Time:  O(n * m)
Space: O(1)

n = Length of array
m = Length of shortest str

=============== Algorithm ===============
1. Start with empty common prefix
2. Iterate over each string (Length of shortest str) times
3. If either 1 str different, return common prefix
4. If found in all str, add to common prefix
'''
def compare_char_of_each_item(strs: list[str]) -> str:
    res = ''

    # Length of shortest str
    for i in range(min(len(s) for s in strs)):
        c = strs[0][i]

        for s in strs:
            # Return if either 1 different
            if s[i] != c: return res
        res += c
    return res

'''
Better for list of long strs (Only compare 2 most lexicographically different strs)

=============== Complexity ===============
Time:  O(n log n + m)
Space: O(1)

n = Length of array
m = Length of shortest str

=============== Algorithm ===============
1. Sort list
2. Compare each char of 2 most different list item
3. If either 1 str different, return common prefix
4. If found in all str, add to common prefix
'''
def compare_2_most_different(strs: list[str]) -> str:
    res = ''
    strs.sort()
    first, last = strs[0], strs[-1]

    for i in range(min(len(first), len(last))):
        if(first[i] != last[i]): return res
        res += first[i]
    return res
