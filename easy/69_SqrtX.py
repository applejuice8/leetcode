'''
=============== Complexity ===============
Time:  O(√x)
Space: O(1)

=============== Algorithm ===============
1. Return x for 0, 1
2. Increment i until i^2 > x
3. Return floor
'''
def linear_search(x: int) -> int:
    if x < 2:
        return x

    i = 2
    while i * i <= x:
        i += 1
    return i - 1

'''
=============== Complexity ===============
Time:  O(log x)
Space: O(1)

=============== Algorithm ===============
1. Binary search
2. If loop exit, means left > right, return floor = right
'''
def halved_binary_search(x: int) -> int:
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid

        if sq == x:
            return mid
        elif sq < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
