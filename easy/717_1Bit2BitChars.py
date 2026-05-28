'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of bits

=============== Algorithm ===============
1. Iterate over each bit
2. If bit is 1, jump 2 bits, else jump 1
3. When loop ends, bit holding the last bit
4. Return False if last bit 1 (Since that implys 2 bits)
'''

def jump1_jump2(bits: list[int]) -> bool:
    i, n = 0, len(bits) - 1

    while i <= n:
        bit = bits[i]
        i += 2 if bit else 1
    return False if bit else True
