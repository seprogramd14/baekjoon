from itertools import combinations
import math

def decimal(num):
    for i in range(2, int(math.sqrt(num))+1):
        if not num % i:
            return 0
    return 1

def solution(nums):
    answer = []
    for c in combinations(nums, 3):
        num = sum(c)
        if decimal(num):
            answer.append(num)
            
    return len(answer)