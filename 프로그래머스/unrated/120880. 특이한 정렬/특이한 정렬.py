def solution(numlist, n):
    for i in range(len(numlist)):
        numlist[i] -= n
    numlist.sort(key = lambda x: (-abs(x), x), reverse=True)
    for i in range(len(numlist)):
        numlist[i] += n
    return numlist