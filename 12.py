def solve(part1: bool):
    def expand(start):
        group = {start}
        while True:
            N = len(group)
            new_nodes = set()
            for a in group:
                for b in graph[a]:
                    new_nodes.add(b)
            group = group.union(new_nodes)
            if len(group) == N:
                return group

    graph = {}
    for line in open("input.txt"):
        l, r = line.strip().split("<->")
        r = r.replace(",", "").strip().split()
        r = [v.strip() for v in r]
        l = l.strip()
        graph[l] = r
        for n in r:
            if n in graph:
                if l in graph[n]:
                    continue
                graph[n].append(l)
            else:
                graph[n] = [l]
    
    if part1: 
        print(len(expand("0")))
    else:
        ngroups = 0
        visited = set()
        for node in graph:
            if node in visited:
                continue
            group = expand(node)
            ngroups += 1
            visited = visited.union(group)
        print(ngroups)


if __name__ == '__main__':
    solve(True)
    solve(False)
