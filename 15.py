def solve(part1: bool):
    v1, v2 = 516, 190
    f1, f2 = 16807, 48271
    div = 2147483647 
    mask = 2**16 - 1
    mult1, mult2 = 4, 8

    def next_value(value, factor, mult):
        while True:
            value = value * factor % div
            if value & (mult - 1) == 0:
                return value

    ans = 0
    cnt = 40000000 if part1 else 5000000
    
    for k in range(cnt):
        if k % 100000 == 0:
            print(k)
        if part1:
            v1 = v1 * f1 % div
            v2 = v2 * f2 % div 
        else:
            v1 = next_value(v1, f1, mult1)
            v2 = next_value(v2, f2, mult2)
        ans += v1 & mask == v2 & mask
    print(ans)
    
if __name__ == '__main__':
    solve(True)
    solve(False)