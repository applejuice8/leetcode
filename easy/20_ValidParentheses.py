'''
=============== Complexity ===============
Time:  O(n)
Space: O(n)

n = Length of array

=============== Algorithm ===============
1. Init hash map for close: open brac
2. Loop through array
3. If open brac, add to stack
4. If close brac, check if top of stack is its corresponding open brac
4. If it's its open brac, pop from stack
5. If it's not its open brac, return False
'''

def use_stack(s: str) -> bool:
    stack = []
    brac_pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for brac in s:
        # Close brac
        if brac in brac_pairs:
            # Remove open brac if top of stack
            if stack and stack[-1] == brac_pairs[brac]:
                stack.pop()
            else:
                return False
        
        # Open brac
        else:
            stack.append(brac)
    return not stack
