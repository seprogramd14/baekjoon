def solution(s):
    answer = []
    l, r = -1, -1
    if 'l' in s: l = s.index('l')
    if 'r' in s: r = s.index('r')
    if l == -1:
        if r == -1: return []
        else: return s[r+1:]
    elif r == -1:
        if l == -1: return []
        else: return s[:l]
    else:
        if l < r: return s[:l]
        else: return s[r+1:]