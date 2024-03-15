from itertools import combinations
def solution(number):
    answer = 0
    for c in combinations(number, 3):
        answer += 0 if sum(c) else 1
    return answer