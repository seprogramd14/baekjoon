def solution(my_string):
    answer, i = 0, 0
    while i < len(my_string):
        buffer, _i = '', 0
        try:
            _i = int(my_string[i])
            for j in range(i, len(my_string)):
                try:
                    int(my_string[j])
                    buffer += my_string[j]
                    i += 1
                except:
                    break
            answer += int(buffer)
            print(buffer)
        except:
            i += 1
            continue
    return answer