'''
=============== Complexity ===============
Time:  O(n)
Space: O(1)

n = Length of s

=============== Algorithm ===============
1. 2 pointers, 1 start 1 end
2. increment left / decrement right until all alphabets
3. Compare 2 alphabets
4. Move both pointers in if same
'''

def two_pointers(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        # Skip non-alphabets
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        
        # Compare left, right
        if s[l].lower() != s[r].lower():
            return False
        
        # Move both pointers in
        l += 1
        r -= 1
    return True
