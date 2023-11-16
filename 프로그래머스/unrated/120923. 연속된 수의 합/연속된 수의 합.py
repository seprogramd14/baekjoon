def _round(n):
    if n < 0:
        if n - int(n) <= 0.5:
            return int(n)
        else:
            return int(n) - 1
    else:
        if n - int(n) >= 0.5:
            return int(n) + 1
        else:
            return int(n)

def solution(num, total):
    center = (total * 2 // num) / 2 # 중앙값
    start = _round(center - num // 2) # 시작값
    return [i for i in range(start, start+num)]