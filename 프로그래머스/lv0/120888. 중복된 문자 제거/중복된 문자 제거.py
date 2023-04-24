def solution(my_string):
    answer = ''
    dic = {i:0 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "}
    for i in my_string:
        if dic[i] == 0:
            dic[i] += 1
            answer += i
    return answer