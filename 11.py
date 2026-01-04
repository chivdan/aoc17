def dist(x, y, z):
    return (abs(x) + abs(y) + abs(z)) // 2


def solve(part1: bool):
    moves = {"n": (0, 1, -1),
             "ne": (1, 0, -1),
             "se": (1, -1, 0),
             "s": (0, -1, 1),
             "sw": (-1, 0, 1),
             "nw": (-1, 1, 0)
             }

    x, y, z = 0, 0, 0
    max_dist = 0
    for move in open("input.txt").read().strip().split(","):
        dx, dy, dz = moves[move]
        x += dx
        y += dy
        z += dz
        max_dist = max(max_dist, dist(x, y, z)) 

    if part1:
        print(dist(x, y, z))
    else:
        print(max_dist)

if __name__ == '__main__':
    solve(True)
    solve(False)
