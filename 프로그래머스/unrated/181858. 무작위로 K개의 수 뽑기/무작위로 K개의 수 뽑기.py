def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
        if len(answer) == k:
            break
    if k > len(answer): answer += [-1 for _ in range(k-len(answer))]
    return answer