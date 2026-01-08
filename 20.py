def solve(part1: bool):
    point, velocity, acceleration = [], [], []
    for line in open("input.txt"):
        p, v, a = [[int(value) for value in v.strip()[3:-1].split(",")] for v in line.split(", ")]
        point.append(p)
        velocity.append(v)
        acceleration.append(a)

    def step():
        for i in range(len(point)):
            for j in range(3):
                velocity[i][j] += acceleration[i][j]
            for j in range(3):
                point[i][j] += velocity[i][j]

    if part1:
        for _ in range(1000):
           step()

        dist = 1e10
        best = None
        for i in range(len(point)):
            d = sum([abs(v) for v in point[i]])
            if d < dist:
                best = i
                dist = d

        print(best)
    else:
        for _ in range(1000):
            step()
            
            positions = dict()
            for i, p in enumerate(point):
                tpl = tuple(p)
                if tpl in positions:
                    positions[tpl] += [i]
                else:
                    positions[tpl] = [i]

            positions_to_remove = set()
            for tpl in positions:
                if len(positions[tpl]) > 1:
                    for p in positions[tpl]:
                        positions_to_remove.add(p)

            point = [point[i] for i in range(len(point)) if i not in positions_to_remove]
            velocity = [velocity[i] for i in range(len(velocity)) if i not in positions_to_remove]
            acceleration = [acceleration[i] for i in range(len(acceleration)) if i not in positions_to_remove]
        
        print(len(point))
                   

if __name__ == '__main__':
    solve(True)
    solve(False)
