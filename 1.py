
def solve(part1: bool):
    s = open("input.txt").read().strip()
    increment = 1 if part1 else len(s) // 2
    result = sum(int(s[i]) if s[i] == s[(i + increment) % len(s)] else 0 for i in range(len(s)))
    print(result)

if __name__ == '__main__':
    solve(True)
    solve(False)