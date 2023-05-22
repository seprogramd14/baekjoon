def solution(a, b, n):
    answer = 0
    while True:
        answer, n = n//a * b + answer, n - (n//a) * a + (n//a) * b
        if n // a <= 0: break
    return answer
