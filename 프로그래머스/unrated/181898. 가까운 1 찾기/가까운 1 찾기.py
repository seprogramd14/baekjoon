def solution(arr, idx):
    answer = [i for i in range(idx, len(arr)) if arr[i] == 1]
    return answer[0] if answer else -1