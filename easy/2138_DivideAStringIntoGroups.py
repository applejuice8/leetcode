'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Length of s

=============== Algorithm ===============
1. Iterate, accumulate each char
2. Once length reach k, append to list and reset word
3. If last word not long enough, fill (k - len) times
'''

def append_when_length_k(s: str, k: int, fill: str) -> list[str]:
    group = []
    word = ''

    # Append when long enough
    for char in s:
        word += char
        if len(word) == k:
            group.append(word)
            word = ''
    
    # Fill empty
    if word:
        word += fill * (k - len(word))
        group.append(word)
    return group
