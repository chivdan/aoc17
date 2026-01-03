def solve(part1: bool):
    inst = [int(v.strip()) for v in open("input.txt")]

    i = 0
    cnt = 0
    while True:
        offset = inst[i]
        if part1 or offset < 3:
            inst[i] += 1
        else:
            inst[i] -= 1
        i += offset
        cnt += 1
        if i < 0 or i >= len(inst):
            break

    print(cnt)


if __name__ == '__main__':
    solve(True)
    solve(False)
