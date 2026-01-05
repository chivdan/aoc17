from functools import reduce
from operator import xor

def knot_hash(input_string: str):
    lengths = [ord(v) for v in input_string] + [17, 31, 73, 47, 23]
   
    a = list(range(256))

    pos = 0
    skip = 0

    L = len(a)

    rounds = 64
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

    return ans

def pad(s):
    return "0" * (4 - len(s)) + s

def neighbors(p):
    i, j = p
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0:
                continue
            if abs(di) + abs(dj) > 1:
                continue
            yield i + di, j + dj

def solve(part1: bool):
    seed = "hwlqcszp"

    nodes = set()
    for i in range(128):
        s = f"{seed}-{i}"
        h = knot_hash(s)
        row = []
        for c in h:
            b = bin(int(c, base=16))[2:]
            row.extend([symb == "1" for symb in pad(b)])
        for j in range(len(row)):
            if row[j]:
                nodes.add((i, j))
    
    if part1:
        print(len(nodes))
        return

    def expand(start):
        group = {start}
        while True:
            N = len(group)
            new_nodes = set()
            for a in group:
                for b in neighbors(a):
                    if b in nodes:
                        new_nodes.add(b)
            group = group.union(new_nodes)
            if len(group) == N:
                return group
    
    
    visited = set()
    ngroups = 0
    for node in nodes:
        if node in visited:
            continue
        group = expand(node)
        ngroups += 1
        visited = visited.union(group)
    print(ngroups)
    
if __name__ == '__main__':
    solve(True)
    solve(False)