def solution(n):
    answer = []
    for pri in range(2, n+1):
        while True:
            if n % pri == 0:
                answer.append(pri)
                n /= pri
            else: break
    return sorted(list(set(answer)))