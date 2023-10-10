def solution(strArr):
    answer = [0] * 30
    for i in range(len(strArr)):
        answer[len(strArr[i])-1] += 1
    return max(answer)