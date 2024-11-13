import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

def backtrack(num, ls):
    if len(ls) == m:
        print(*ls)
        return
    check = [0] * 10001
    for i in range(len(num)):
        answer = ls.copy()
        if len(answer) < m:
            if not check[num[i]]:
                check[num[i]] = 1
                answer.append(num[i])
                backtrack(num[:i]+num[i+1:], answer)

backtrack(num, [])