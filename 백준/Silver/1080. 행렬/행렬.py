import sys
input = sys.stdin.readline

n, m = map(int, input().split())
org = [[int(i) for i in input().rstrip()] for _ in range(n)]
last = [[int(i) for i in input().rstrip()] for _ in range(n)]

def change(x, y):
    for i in range(3):
        for j in range(3):
            org[x+i][y+j] = 1 - org[x+i][y+j]

ch = 0
for i in range(n-2):
    for j in range(m-2):
        if org[i][j] != last[i][j]:
            change(i, j)
            ch += 1

for i in range(n):
    for j in range(m):
        if org[i][j] != last[i][j]:
            print(-1)
            exit()
print(ch)