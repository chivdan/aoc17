def solve(part1: bool):
    s = [chr(c) for c in range(ord('a'), ord('p') + 1)]
    L = len(s)    

    commands = [cmd for cmd in open("input.txt").read().strip().split(",")]
        
    def dance(l):
        s = [c for c in l]
        for cmd in commands:
            if cmd[0] == "s":
                x = int(cmd[1:])
                s = s[L - x:]  + s[:L - x]
            elif cmd[0] == "x":
                a, b = [int(v) for v in cmd[1:].split("/")]
                s[a], s[b] = s[b], s[a]
            elif cmd[0] == "p":
                a, b = cmd[1:].split("/")
                ia = s.index(a)
                ib = s.index(b)
                s[ia], s[ib] = s[ib], s[ia]
        return "".join(s)

    N = 1 if part1 else (1000000000 % 36)

    s = "".join(s)
    for i in range(N):
        s = dance(s) 
            
    print(s)

if __name__ == '__main__':
    solve(True)
    solve(False)