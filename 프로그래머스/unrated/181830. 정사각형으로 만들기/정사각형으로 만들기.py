def solution(arr):
    answer = [[]]
    l1, l2 = len(arr), len(arr[0])
    if l1 > l2:
        for i in range(l1):
            arr[i] += [0] * (l1 - l2)
    elif l1 < l2:
        for i in range(l2 - l1):
            arr.append([0] * l2)
    return arr