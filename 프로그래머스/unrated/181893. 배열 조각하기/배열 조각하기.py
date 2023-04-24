def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        if i % 2 == 0: answer = answer[:query[i]+1]
        else: answer = answer[query[i]:]
    return answer