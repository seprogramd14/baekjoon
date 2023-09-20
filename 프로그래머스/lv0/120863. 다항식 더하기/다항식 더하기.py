def solution(polynomial):
    poly = polynomial.split(' + ')
    answer = [0, 0] # x의 계수, 상수항
    for i in poly:
        if 'x' in i:
            i = i.split('x')
            answer[0] += int(i[0]) if i[0] else 1
        else:
            answer[1] += int(i)
    x = str(answer[0]) + 'x' if answer[0] != 1 else 'x'
    c = str(answer[1]) if answer[1] != 0 else ''
    if c and answer[0] != 0: result = x + ' + ' + c
    elif answer[0] != 0: result = x
    else: result = c
    return result