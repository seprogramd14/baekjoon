def solution(num_list):
    answer1, answer2 = '', ''
    for num in num_list:
        if num % 2 == 0: answer2 += str(num)
        else: answer1 += str(num)
    return int(answer1) + int(answer2)