def solve(part1: bool):
    comp_map = {'<': lambda x, y: x < y,
                '>': lambda x, y: x > y,
                '<=': lambda x, y: x <= y,
                '>=': lambda x, y: x >= y,
                '==': lambda x, y: x == y,
                '!=': lambda x, y: x != y}

    reg = dict()
    max_val = 0
    for line in open("input.txt"):
        s = line.strip().split()
        r, cmd, val, _, cond_r, comp, comp_val = s
        val = int(val)
        comp_val = int(comp_val)
        if comp_map[comp](reg.get(cond_r, 0), comp_val):
            reg[r] = reg.get(r, 0) + (-1 if cmd == "dec" else 1) * val
            max_val = max(max_val, reg[r])

    if part1:
        print(max(reg.values()))     
    else:
        print(max_val)
    
if __name__ == '__main__':
    solve(True)
    solve(False)