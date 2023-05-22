def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        fruit_box = []
        for _ in range(m):
            fruit_box.append(score.pop())
        answer += min(fruit_box) * m
    return answer
