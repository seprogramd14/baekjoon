def solution(before, after):
    answer = 1
    for i in after:
        if before.count(i) != after.count(i): answer = 0; break
    return answer