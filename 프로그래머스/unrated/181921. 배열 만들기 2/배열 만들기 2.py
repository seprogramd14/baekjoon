def solution(l, r):
    answer = []
    for i in range(l, r+1):
        i_ = str(i).translate({ord(x) : None for x in '12346789'})
        if str(i) == i_: answer.append(i)
    return answer if answer else [-1]