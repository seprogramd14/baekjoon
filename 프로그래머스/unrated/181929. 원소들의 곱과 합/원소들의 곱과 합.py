def solution(num_list):
    answer1, answer2 = 1, 0
    for i in num_list:
        answer1 *= i
        answer2 += i
    return 0 if answer1 > answer2**2 else 1