from itertools import combinations
def solution(number):
    return sum([0 if sum(c) else 1 for c in combinations(number, 3)])