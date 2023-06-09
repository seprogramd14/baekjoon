def solution(my_string):
    answer = 0
    my_string = my_string.split(' ')
    for i in range(0, len(my_string), 2):
        if i == 0: answer = int(my_string[i])
        elif my_string[i-1] == "+": answer += int(my_string[i])
        elif my_string[i-1] == "-": answer -= int(my_string[i])
    return answer