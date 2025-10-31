lows = [1,2,3,4,5]
highs = [9,7,5,7,8]

for low in lows:
    for high in highs:
        mid = low + (high - low) // 2
        print(f'{mid}, ', end='')
        mid = (low + high) // 2
        print(mid)
