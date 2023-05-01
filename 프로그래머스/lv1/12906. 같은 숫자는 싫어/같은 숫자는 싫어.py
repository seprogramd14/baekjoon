def solution(arr):
    answer = [arr[0]]
    for idx in range(1, len(arr)):
        if answer[-1] != arr[idx]: answer.append(arr[idx])
    return answer