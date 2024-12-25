import sys
input = sys.stdin.readline

_, p1, p2 = map(int, input().split())

cnt = 1
while (p1:=p1//2 + p1%2) != (p2:=p2//2 + p2%2):
    cnt += 1
print(cnt)