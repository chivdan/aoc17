def solve(part1: bool):
    fsm = dict()

    lines = [line.strip() for line in open("input.txt")]
    
    start = lines[0].strip().split()[-1][:-1]
    N = int(lines[1].strip().split()[-2])

    i = 2
    while i < len(lines):
        if "In state" in lines[i]:
            state = lines[i].strip().split()[-1][:-1]
            tr = {0: [], 1: []}
            tr[0].append(int(lines[i + 2].strip().split()[-1][:-1]))
            tr[0].append(1 if lines[i + 3].strip().split()[-1][:-1] == "right" else -1)
            tr[0].append(lines[i + 4].strip().split()[-1][:-1])
            
            tr[1].append(int(lines[i + 6].strip().split()[-1][:-1]))
            tr[1].append(1 if lines[i + 7].strip().split()[-1][:-1] == "right" else -1)
            tr[1].append(lines[i + 8].strip().split()[-1][:-1])
            
            fsm[state] = tr
            i += 8
        else:
            i += 1  

    state = start
    tape = dict()
    pos = 0
    for _ in range(N):
        value = tape.get(pos, 0)
        tr = fsm[state][value]
        write = tr[0]
        move = tr[1]
        nxt = tr[2]
        tape[pos] = write
        pos += move
        state = nxt

    print(sum(tape.values()))
    
if __name__ == '__main__':
    solve(True)
