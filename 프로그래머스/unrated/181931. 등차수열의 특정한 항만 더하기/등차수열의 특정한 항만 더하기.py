def solution(a, d, included):
    answer = 0
    Sum = a
    for i in range(len(included)):
        if included[i]: answer += Sum
        Sum += d
    return answer