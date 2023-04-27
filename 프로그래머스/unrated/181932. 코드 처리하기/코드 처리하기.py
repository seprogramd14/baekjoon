def solution(code):
    answer = ''
    mode = 0
    ret = ''
    for i in range(len(code)):
        if code[i] == '1':
            mode = 1 if mode != 1 else 0
        else:
            if mode: # true
                if i % 2 != 0: ret += code[i]
            else:
                if i % 2 == 0: ret += code[i]
    answer = ret if ret else "EMPTY"
    return answer