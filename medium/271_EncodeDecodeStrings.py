'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Total chars in list

=============== Algorithm ===============
1. When encode, store list of strings into a single string with their length ['hello', 'joseph'] -> '5#hello6#joseph'
2. When decode, read length then slice the string and append list
'''

def encode(strs: list[str]) -> str:
    res = ''
    for s in strs:
        res += f'{len(s)}#{s}'
    return res

def decode(s: str) -> list[str]:
    i = 0
    res = []

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        
        length = int(s[i:j])  # Length is index until delimeter
        i = j + length + 1  # Index of next length
        res.append(s[j+1:i])  # 1 char after delimeter until index of next length
    return res
