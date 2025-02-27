import sys
input = sys.stdin.readline

n, l = map(int, input().split())
while True:
    res = n/l - (l-1)/2
    if res < 0 or l > 100:
        print(-1)
        exit()
    elif int(res) == res:
        print(*[i for i in range(int(res), int(res)+l)])
        break
    else:
        l += 1