def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    answer += '0' + answer[::-1] # 이거 기억 좀 하자.
    return answer
