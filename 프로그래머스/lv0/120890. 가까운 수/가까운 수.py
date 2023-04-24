def solution(array, n):
    answer = 0
    array.append(n)
    array.sort()
    idx = array.index(n)
    if 0 < idx < len(array)-1:
        if array[idx + 1] - array[idx] < array[idx] - array[idx-1]: answer = array[idx + 1]
        else: answer = array[idx-1]
    elif idx == 0: answer = array[1]
    else: answer = array[-2]
    return answer