def solution(num_list):
    answer = [i for i in range(len(num_list)) if num_list[i] < 0]
    return answer[0] if answer else -1