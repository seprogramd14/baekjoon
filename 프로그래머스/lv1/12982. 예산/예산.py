def solution(d, budget):
    answer = 0
    for i in sorted(d):
        if budget >= i:
            budget, answer = budget - i, answer + 1
    return answer