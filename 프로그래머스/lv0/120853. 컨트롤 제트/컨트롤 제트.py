def solution(s):
    answer = 0
    save = 0
    lst = s.split()
    for i in lst:
        if i == "Z":
            answer -= save
        else:
            save = int(i)
            answer += int(i)
    return answer