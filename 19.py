def solve(part1: bool):
    m = []
    for line in open("input.txt"):
        row = [c for c in line[:-1]]
        m.append(row)
   
    def step(i, j, d):
        if d == "n":
            return i - 1, j
        elif d == "s":
            return i + 1, j
        elif d == "w":
            return i, j - 1
        elif d == "e":
            return i, j + 1
        raise ValueError("unknown direction")

    def neighbors(i, j):
        return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    
    def out_of_range(i, j):
        return i < 0 or i >= len(m) or j < 0 or j >= len(m[i])
                
    def move(i, j, d):
        letters = []
        cnt = 1
        while True:
            if out_of_range(i, j):
                break
            ni, nj = step(i, j, d)
            if out_of_range(ni, nj):
                break
            if m[ni][nj] == "+":
                # turn
                cnt += 1
                for dd in "snwe":
                    ti, tj = step(ni, nj, dd)
                    if out_of_range(ti, tj):
                        continue
                    if (ti, tj) == (i, j):
                        continue
                    if m[ti][tj] == " ":
                        continue
                    d = dd
                    break
            elif m[ni][nj] not in " -|+":
                letters.append(m[ni][nj])
                cnt += 1
            elif m[ni][nj] == " ":
                break
            elif m[ni][nj] in "-|":
                cnt += 1
            i, j = ni, nj
        return letters, cnt
        
 
    i, j = 0, m[0].index("|")
    d = "s"
    
    letters, dist = move(i, j, d)

    if part1:
        print("".join(letters))
    else:
        print(dist)

if __name__ == '__main__':
    solve(True)
    solve(False)
