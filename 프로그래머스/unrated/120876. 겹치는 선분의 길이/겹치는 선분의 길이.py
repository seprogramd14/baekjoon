def solution(lines):
    [[4, 7], [4, 5], [6, 7]]
    max_v, min_v =  max(map(max, lines)), min(map(min, lines))
    line = []
    if min_v < 0:
        line = [0 for i in range(max_v - min_v)]
    else:
        line = [0 for i in range(max_v)]
    for l in lines:
        for i in range(l[0], l[1]):
            line[i] += 1
    line = [i for i in line if i > 1]
    return len(line)