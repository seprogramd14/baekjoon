def solution(myString, pat):
    answer = 0
    if pat in myString:
        answer = len(myString) - myString[::-1].index(pat[-1])
    return myString[:answer]