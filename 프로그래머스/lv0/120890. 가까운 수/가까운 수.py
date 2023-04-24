def solution(array, n):
    # 각 값의 격차를 확인
    array.sort(key = lambda x : (abs(x-n), x-n)) # 마이너스는 절댓값으로
    return array[0]