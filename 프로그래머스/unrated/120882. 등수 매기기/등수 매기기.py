def solution(score):
    answer = []
    for sc in score:
        answer.append((sc[0] + sc[1]) * 10)
    a1 = sorted(answer, reverse=True)
    buffer, count = 0, [1, 0]
    for a in a1:
        idx = answer.index(a)
        if a != buffer:
            buffer = a
            answer[idx] = count[0]
            count[1] = 0
        else:
            count[1] += 1
            answer[idx] = count[0] - count[1]
        count[0] += 1
    return answer