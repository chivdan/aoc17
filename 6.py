def solve(part1: bool):
    m = [int(v.strip()) for v in open("input.txt").read().split()]

    seen = dict()
    seen[tuple(m)] = 0
    while True:
        max_value = max(m)
        max_i = m.index(max_value)
        m[max_i] = 0
        i = (max_i + 1) % len(m)
        while max_value > 0:
            m[i] += 1
            max_value -= 1
            i = (i + 1) % len(m)
        tpl = tuple(m)
        if tpl in seen:
            if part1:
                print(len(seen))
            else:
                print(len(seen) - seen[tpl])
            break
        seen[tpl] = len(seen)

    
if __name__ == '__main__':
    solve(True)
    solve(False)
