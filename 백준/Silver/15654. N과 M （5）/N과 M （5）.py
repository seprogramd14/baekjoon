import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
num = sorted(list(map(int, input().split())))

def backtrack(ls):
    for i in range(n):
        answer = ls.copy()
        if len(answer) < m:
            if num[i] not in answer:
                answer.append(num[i])
                backtrack(answer)
        else:
            print(*answer)
            return
        
for i in range(n):
    backtrack([num[i]])