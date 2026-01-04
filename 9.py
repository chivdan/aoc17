def solve(part1: bool):
    s = open("input.txt").read()
    ans = 0    
    score = 0
    garbage = False
    garbage_count = 0
    i = 0
    while i < len(s):
        c = s[i]   
        if garbage and c == "!":
            # ingore character in garbage
            i += 2
            continue
        if garbage and c != ">":
            # don't care about any characters in garbage
            i += 1
            garbage_count += 1 
            continue     
        if garbage and c == ">":    
            garbage = False
            i += 1
            continue

        if not garbage and c == "<":
            garbage = True
            i += 1
            continue

        if c == "{":
            score += 1
        elif c == "}" and score > 0:
            ans += score
            score -= 1
        i += 1

    if part1:
        print(ans)
    else:
        print(garbage_count)

    
if __name__ == '__main__':
    solve(True)
    solve(False)