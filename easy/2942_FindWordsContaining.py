'''
=============== Complexity ===============
Time:  O(m * n)
Space: O(k)

n = Length of array
m = Average length of each word
k = Length of res

=============== Algorithm ===============
1. Iterate each word
2. If x in word, append index
3. Return all indices
'''

def iterate_with_index(words: list[str], x: str) -> list[int]:
    res = []
    for i, word in enumerate(words):
        if x in word:
            res.append(i)
    return res
