def solution(dartResult):
    answer, save, cut = 0, [], 0 # 더 보기 좋은 답은 얼마든지 있다
    for i in range(len(dartResult)):
        try:
            if dartResult[i:i+2] == '10':
                save.append(10)
                cut = 1
            elif cut == 1: cut = 0
            else: save.append(int(dartResult[i]))
        except:
            if dartResult[i] == "S": save[-1] **= 1
            elif dartResult[i] == "D": save[-1] **= 2
            elif dartResult[i] == "T": save[-1] **= 3
            elif dartResult[i] == "*":
                save[-1] *= 2
                if len(save) > 1: save[-2] *= 2
            elif dartResult[i] == "#": save[-1] *= -1
    return sum(save)