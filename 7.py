def solve(part1: bool):
    def weight(node):
        result = weights[node]
        if node not in tree:
            return result
        for child in tree[node]:
            result += weight(child)
        return result

    def find_mismatch(node, diff, ans):
        cw = [(weight(c), c) for c in tree[node]]
        cw.sort(reverse=True)
        if cw[0][0] - cw[1][0] == diff:
            child = cw[0][1]
            ans = weights[cw[0][1]] - diff
            if child in tree:
                find_mismatch(child, diff, ans)
        else:
            print(ans)

    nodes = set()
    children = set()
    weights = dict()
    tree = dict()
    for line in open("input.txt"):
        s = line.strip().split()
        w = int(s[1][1:-1])
        l = s[0]
        nodes.add(l)
        weights[l] = w
        if "->" in s:
            r = [v.replace(",", "") for v in s[3:]]
            for n in r:
                nodes.add(n)
                children.add(n)
            tree[l] = r

    bottom = list(nodes.difference(children))[0]

    if part1:
        print(bottom)
    else:
        bottom_weights = [weight(c) for c in tree[bottom]]
        diff = max(bottom_weights) - min(bottom_weights)
        find_mismatch(bottom, diff, None)

if __name__ == '__main__':
    solve(True)
    solve(False)
