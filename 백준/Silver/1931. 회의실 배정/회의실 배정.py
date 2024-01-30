import sys
input = sys.stdin.readline

n = int(input())
time = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x : (x[1], x[0]))
answer = 1
t = time[0]
for i in range(1, n):
    if time[i][0] >= t[1]:
        t = time[i]
        answer += 1
print(answer)