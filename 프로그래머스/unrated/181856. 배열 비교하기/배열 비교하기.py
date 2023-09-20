def solution(arr1, arr2): # arr1이 크면 1 같으면 0 arr2가 크면-1
    if len(arr1) > len(arr2) or len(arr1) == len(arr2) and sum(arr1) > sum(arr2):
        return 1
    elif len(arr1) < len(arr2) or len(arr1) == len(arr2) and sum(arr1) < sum(arr2):
        return -1
    return 0