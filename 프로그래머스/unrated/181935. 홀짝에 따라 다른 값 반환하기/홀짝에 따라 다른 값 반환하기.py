def solution(n):
    Sum = 0
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0: Sum += i*i
    else:
        for i in range(1, n+1):
            if i % 2 != 0: Sum += i
    return Sum