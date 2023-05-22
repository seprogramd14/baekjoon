def solution(a, b, n):
    answer = 0
    while n // a > 0: answer, n = n//a * b + answer, n - (n//a) * (a-b)
    return answer