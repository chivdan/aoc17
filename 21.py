import numpy as np
from functools import cache

@cache
def get_variants(pattern_tuple, size):
    pattern = np.zeros((size, size))
    for i, j in pattern_tuple:
        pattern[i][j] = 1
    covered = set()
    covered.add(pattern_tuple)
    options = [pattern]
    for rot in [0, -1, -2, -3]:
        transformed = np.rot90(pattern, rot)
        st = get_ints(transformed)
        if st not in covered:
            options.append(transformed)
            covered.add(st)
        for flip in [np.flipud, np.fliplr]:
            flipped = flip(transformed)
            st = get_ints(flipped)
            if st not in covered:
                options.append(flipped)
                covered.add(st)
    return options

def find_variant(m, i, j, patterns):
    d = len(patterns[0][0])
    for pattern, rhs, tpl, on in patterns:
        if np.sum(m[i:i + d, j:j + d]) != on:
            continue
        for variant in get_variants(tpl, len(pattern)):
            if np.array_equal(m[i:i + d, j:j + d], variant):
                return rhs 
    return None

def get_ints(m):
    ones = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                ones.append((i, j))
    return tuple(sorted(ones))

def solve(part1: bool):
    patterns_2 = []
    patterns_3 = []
    
    for line in open("input.txt"):
        l, r = line.strip().split(" => ")
        l = l.strip().split("/")
        r = r.strip().split("/")
        l = [[int(c == "#") for c in row] for row in l]
        r = [[int(c == "#") for c in row] for row in r]
        if len(l) == 2:
            patterns_2.append((l, r, get_ints(l), np.sum(l)))
        elif len(l) == 3:
            patterns_3.append((l, r, get_ints(l), np.sum(l)))
        else:
            raise Exception()

    m = [[0, 1, 0],
         [0, 0, 1],
         [1, 1, 1]]
    m = np.array(m)

    N = 5 if part1 else 18

    for n in range(N):
        patterns = patterns_2 if len(m) % 2 == 0 else patterns_3
        step = 2 if len(m) % 2 == 0 else 3
        d = len(m) // step 
        new = np.zeros((len(m) + d, len(m) + d))
        di = 0
        for i in range(0, len(m), step):
            dj = 0
            for j in range(0, len(m), step):
                rhs = find_variant(m, i, j, patterns)
                if rhs is None:
                    raise Exception("could not find pattern")
                new[i + di:i + di + step + 1, j + dj:j + dj + step + 1] = rhs
                dj += 1
            di += 1
        m = new

    print(int(np.sum(m)))

if __name__ == '__main__':
    solve(True)
    solve(False)
