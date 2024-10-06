import sys
input = sys.stdin.readline

def hanoi(n, start, mid, end):
    global cnt
    if n != 0:
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)
    return 

n = int(input())
cnt = 1
for i in range(1, n):
    cnt = cnt * 2 + 1
print(cnt)

if n <= 20:
    hanoi(n, 1, 2, 3)