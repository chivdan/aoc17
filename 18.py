class Program:
    def __init__(self, pid, commands, q, other_q):
        self.pid = pid
        self.reg = {"p": pid}
        self.commands = commands
        self.q = q
        self.other_q = other_q
        self.i = 0
        self.sent_cnt = 0

    def value(self, arg):
        if arg.isalpha():
            return self.reg.get(arg, 0)
        return int(arg)

    def step(self):
        if self.i >= len(self.commands):
            return True
        cmd, args = self.commands[self.i]
       
        if cmd == "snd":
            self.other_q.append(self.value(args[0]))
            self.sent_cnt += 1
        elif cmd == "set":
            self.reg[args[0]] = self.value(args[1])        
        elif cmd == "add":
            self.reg[args[0]] = self.reg.get(args[0], 0) + self.value(args[1])
        elif cmd == "mul":
            self.reg[args[0]] = self.value(args[0]) * self.value(args[1])
        elif cmd == "mod":
            self.reg[args[0]] = self.value(args[0]) % self.value(args[1])
        elif cmd == "rcv":
            if self.q:
                self.reg[args[0]] = self.q.pop(0)
            else:
                return False
        elif cmd == "jgz":
            if self.value(args[0]) > 0:
                self.i += self.value(args[1])
                return False

        self.i += 1
        return False

    def is_locked(self):
        return len(self.q) == 0 and self.i < len(self.commands) and self.commands[self.i][0] == "rcv"



def solve(part1: bool):
    reg = dict()

    def value(arg):
        if arg.isalpha():
            return reg.get(arg, 0)
        return int(arg)
    
    sound = None
    
    commands = []
    for line in open("input.txt"):
        s = line.strip().split()
        commands.append((s[0], s[1:]))
 
    if part1:
        i = 0
        while i < len(commands):
            cmd, args = commands[i]
       
            if cmd == "snd":
                sound = value(args[0])
            elif cmd == "set":
                reg[args[0]] = value(args[1])        
            elif cmd == "add":
                reg[args[0]] = reg.get(args[0], 0) + value(args[1])
            elif cmd == "mul":
                reg[args[0]] = value(args[0]) * value(args[1])
            elif cmd == "mod":
                reg[args[0]] = value(args[0]) % value(args[1])
            elif cmd == "rcv":
                if value(args[0]) != 0:
                    print(sound)
                    break
            elif cmd == "jgz":
                if value(args[0]) > 0:
                    i += value(args[1])
                    continue
            i += 1
    else:
        q0, q1 = [], []
        p0 = Program(0, commands, q0, q1)
        p1 = Program(1, commands, q1, q0)

        while True:
            p0_done = p0.step()
            p1_done = p1.step()
            if p0_done and p1_done:
                print(p1.sent_cnt)
                break

            if p0.is_locked() and p1.is_locked():
                print(p1.sent_cnt)
                break

if __name__ == '__main__':
    solve(True)
    solve(False)
