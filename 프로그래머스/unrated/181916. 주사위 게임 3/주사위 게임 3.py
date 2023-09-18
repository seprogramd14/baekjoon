from collections import Counter
def solution(a, b, c, d):
    cnt = dict(Counter([a, b, c, d]))
    val = sorted(cnt.items(), key=lambda x : x[1])
    if val[-1][1] == 4: return val[-1][0] * 1111
    elif val[-1][1] == 3: return (10 * val[-1][0] + val[-2][0]) ** 2
    elif val[-1][1] == 2 and val[-2][1] == 2:
        return (val[-1][0] + val[-2][0]) * abs(val[-1][0] - val[-2][0])
    elif val[-1][1] == 2: return val[-2][0] * val[-3][0]
    else: return min(cnt)