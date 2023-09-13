def solution(arr, queries):
    answer = []
    for i, j, g in queries:
        for x in range(i, j+1):
            if x % g == 0: arr[x] += 1
    return arr