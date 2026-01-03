def solve(part1: bool):
    result = 0
    for line in open("input.txt"):
        s = line.strip().split()
        if part1:
            if len(s) > 1 and len(set(s)) == len(s):
                result += 1
        else:
            if len(set("".join(sorted(w)) for w in s)) == len(s):
                result += 1
    print(result)


if __name__ == '__main__':
    solve(True)
    solve(False)
