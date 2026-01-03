def divisible_pair(row):
    row.sort()
    for i in range(len(row)):
        for j in range(i):
            if row[i] % row[j] == 0:
                return row[i], row[j]
    return None


def solve(part1: bool):
    result = 0    
    for line in open("input.txt"):
        row = [int(v) for v in line.strip().split()]
        if part1:
            result += max(row) - min(row)
        else:
            a, b = divisible_pair(row)
            result += a // b
            
    print(result)

if __name__ == '__main__':
    solve(True)
    solve(False)