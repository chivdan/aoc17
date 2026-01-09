def move(i, j, d):
    if d == "n":
        return i - 1, j
    elif d == "s":
        return i + 1, j
    elif d == "w":
        return i, j - 1
    elif d == "e":
        return i, j + 1

def solve(part1: bool):
    turn = {"n": {"l": "w", "r": "e"},
            "e": {"l": "n", "r": "s"},
            "s": {"l": "e", "r": "w"},
            "w": {"l": "s", "r": "n"}
            }

    m = dict()
    i = 0
    for line in open("input.txt"):
        for j, c in enumerate(line.strip()):
            if part1:
                m[(i, j)] = int(c == "#")
            else:
                m[(i, j)] = 0 if c == "." else 2
                    

        i += 1

    i, j = i // 2, i // 2
    d = "n"
    n_infected = 0

    N = 10000 if part1 else 10000000

    for _ in range(N):
        if part1:
            if m.get((i, j), 0) == 1:
                d = turn[d]["r"]
                m[(i, j)] = 0 
            else:
                d = turn[d]["l"]
                m[(i, j)] = 1
                n_infected += 1
        else:
            state = m.get((i, j), 0)
            if state == 0:
                #clean
                d = turn[d]["l"]
            elif state == 1:
                #weakened
                pass
            elif state == 2:
                #infected
                d = turn[d]["r"]
            elif state == 3:
                #flagged
                d = turn[d]["r"]
                d = turn[d]["r"]

            m[(i, j)] = (state + 1) % 4
            if m[(i, j)] == 2:
                n_infected += 1

        i, j = move(i, j, d)

    print(n_infected)

if __name__ == '__main__':
    solve(True)
    solve(False)
