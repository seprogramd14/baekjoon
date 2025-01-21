import sys
input = sys.stdin.readline

sinario = 1
while (n:=int(input())) != 0:
    name = [input().rstrip() for _ in range(n)]
    cnt = {i+1:0 for i in range(n)}
    for _ in range(2*n-1):
        num, _ = map(str, input().split())
        cnt[int(num)] += 1
    for k in cnt:
        if cnt[k] == 1:
            print(sinario, name[k-1])
            break
    sinario += 1