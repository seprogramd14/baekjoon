def solution(spell, dic):
    for i in range(len(dic)):
        answer = 0
        for j in spell:
            if j in dic[i]: answer += 1
        if answer == len(spell): return 1
    return 2