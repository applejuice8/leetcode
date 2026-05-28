'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of s

=============== Algorithm ===============
1. Iterate each char
2. Count vowels, consonants
3. Return sum of vowels, consonants (Or 0 if any absent)
'''

def count_vowels_consonants(s: str) -> int:
    vow, con = {}, {}
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for c in s:
        if c in vowels:
            vow[c] = vow.get(c, 0) + 1
        else:
            con[c] = con.get(c, 0) + 1
    
    max_vow = max(vow.values()) if vow else 0
    max_con = max(con.values()) if con else 0

    return max_vow + max_con
