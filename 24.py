from functools import cache

def solve(part1: bool):
    components = [tuple(sorted([int(v) for v in line.strip().split("/")])) for line in open("input.txt")]

    @cache
    def strength(bridge):
        return sum(sum(c) for c in bridge)
    
    def max_bridge(bridge: list, last_port=None):
        if len(bridge) == 0:
            return max(max_bridge([c], c[1]) for c in components if c[0] == 0)
        children = []
        for comp in components:
            p1, p2 = comp
            if p1 != last_port and p2 != last_port:
                continue
            if comp in bridge:
                continue
            if p1 != p2:
                new_last = [p for p in comp if p != last_port][0]
            else:
                new_last = p2
            children.append((bridge[:] + [comp], new_last))
        
        if len(children) == 0:
            result = strength(tuple(sorted(bridge)))
            if part1:
                return result
            else:
                return len(bridge), result
        return max(max_bridge(*c) for c in children)

    result = max_bridge([])
    if part1:
        print(result)
    else:
        print(result[1])
    
        
if __name__ == '__main__':
    solve(True)
    solve(False)
