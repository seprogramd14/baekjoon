import math
def solution(common):
    answer = []
    for i in range(1, len(common)):
        answer.append(common[i] - common[i-1])
    if len(set(answer)) == 1: # 공차 수열
        return answer[0] + common[-1]
    else: # 공비 수열
        return common[-1] * (common[1] // common[0])