def solution(my_string, is_prefix):
    answer = 1
    for i in range(len(is_prefix)):
        try:
            if my_string[i] != is_prefix[i]: answer = 0
        except:
            answer = 0
    return answer