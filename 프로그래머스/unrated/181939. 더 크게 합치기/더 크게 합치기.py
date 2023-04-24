def solution(a, b):
    answer1 = str(a) + str(b)
    answer2 = str(b) + str(a)
    return int(answer1 if answer1 >= answer2 else answer2)