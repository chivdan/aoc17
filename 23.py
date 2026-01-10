import math

def is_prime(n):
    for d in range(2, int(math.sqrt(n))):
        if n % d == 0:
            return False
    return True

def solve(part1: bool):
    reg = dict()

    def value(arg):
        if arg.isalpha():
            return reg.get(arg, 0)
        return int(arg)
    
    commands = []
    for line in open("input.txt"):
        s = line.strip().split()
        commands.append((s[0], s[1:]))
 
    if part1:
        mul_cnt =0
        i = 0
        while i < len(commands):
            cmd, args = commands[i]
       
            if cmd == "set":
                reg[args[0]] = value(args[1])        
            elif cmd == "sub":
                reg[args[0]] = reg.get(args[0], 0) - value(args[1])
            elif cmd == "mul":
                mul_cnt += 1
                reg[args[0]] = value(args[0]) * value(args[1])
            elif cmd == "jnz":
                if value(args[0]) != 0:
                    i += value(args[1])
                    continue
            i += 1
     
        print(mul_cnt)
    else:
        h = 0
        for b in range(106700, 123700 + 1, 17):
            if not is_prime(b):
                h += 1
        print(h)

if __name__ == '__main__':
    solve(True)
    solve(False)
