from functools import reduce
from operator import xor

def solve(part1: bool):
    if part1:
        lengths = [int(v) for v in open("input.txt").read().split(",")]
    else:
        lengths = [ord(v) for v in open("input.txt").read().strip()] + [17, 31, 73, 47, 23]
   
    a = list(range(256))

    pos = 0
    skip = 0

    L = len(a)

    rounds = 1 if part1 else 64
    for _ in range(rounds):
        for l in lengths:
            if pos + l <= L:
                m = a[:pos] + a[pos:pos+l][::-1] + a[pos + l:]
            else:
                m = a + a
                m = m[:pos] + m[pos:pos + l][::-1] + m[pos + l:]
                
                diff = (pos + l) - L
                for i in range(diff):
                    m[i] = m[L + i]
                m = m[:L]

            a = m
            pos += (l + skip)
            pos = pos % L
            skip += 1

    if part1:
        print(a[0] * a[1])
        return

    m = []
    for i in range(0, len(a), 16):
        m.append(reduce(xor, a[i:i+16]))
    a = m

    ans = ""
    for v in a:
        h = hex(v)[2:]
        if len(h) <= 1:
            h = "0" + h
        ans += h

    print(ans)
    
    
if __name__ == '__main__':
    solve(True)
    solve(False)