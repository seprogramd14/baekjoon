def solution(arr):
    answer = []
    for i in range(11):
        if len(arr) <= 2**i:
            arr += [0 for _ in range(2**i - len(arr))]
            return arr