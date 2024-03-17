import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

def backtrack(ls):
    for i in range(1, n+1):
        answer = ls.copy()
        if len(answer) < m:
            if answer[-1] <= i:
                answer.append(i)
                backtrack(answer)
        else:
            print(*answer)
            return
for i in range(1, n+1):
    backtrack([i])