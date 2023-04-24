def solution(a, b):
    answer = a*a+b*b if a % 2 != 0 and b % 2 != 0 else 2*(a+b) if a % 2 != 0 or b % 2 != 0 else abs(a-b)
    return answer