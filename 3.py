def next_point(p, d):
    i, j = p
    if d == "R":
        return i, j + 1
    elif d == "L":
        return i, j - 1
    elif d == "U":
        return i - 1, j
    elif d == "D":
        return i + 1, j
    raise ValueError(f"Unknown direction {d}")

def turn(d):
    if d == "R":
        return "U"
    elif d == "U":
        return "L"
    elif d == "L":  
        return "D"
    elif d == "D":
        return "R"
    raise ValueError(f"Unknown direction {d}")

def neighbors(p):
    x, y = p
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            yield x + dx, y + dy

def solve(part1: bool):
    number = 361527
 
    p = 0, 0
    occupied = {p}
    value = 1
    d = "R"
    values = {p: 1}
    while value < number:
        p = next_point(p, d)
        occupied.add(p)
        if next_point(p, d) not in occupied and next_point(p, turn(d)) not in occupied:
            d = turn(d)
        if part1:
            value += 1
        else:
            value = sum(values[n] if n in values else 0 for n in neighbors(p))
            values[p] = value

    if part1:
        i, j = p
        print(abs(i) + abs(j))      
    else:
        print(value)
        

if __name__ == '__main__':
    solve(True)
    solve(False)