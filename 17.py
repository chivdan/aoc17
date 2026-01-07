def solve(part1: bool):
    N = 394
    pos = 0

    if part1:
        buf = [0]
        for i in range(1, 2018):
            pos = (pos + N) % i
            pos += 1
            buf.insert(pos, i)

        print(buf[buf.index(2017) + 1]) 
    else:
        ans = None
        for i in range(1, 50000000):
            pos = (pos + N) % i + 1
            if pos == 1:
                ans = i
        print(ans)


if __name__ == '__main__':
    solve(True)
    solve(False)
