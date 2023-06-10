def solution(quiz):
    quiz = [i.split() for i in quiz]
    answer = []
    for ope in quiz:
        if ope[1] == '+' and int(ope[0]) + int(ope[2]) == int(ope[4]): answer.append("O")
        elif ope[1] == '-' and int(ope[0]) - int(ope[2]) == int(ope[4]): answer.append("O")
        else: answer.append("X")
    return answer