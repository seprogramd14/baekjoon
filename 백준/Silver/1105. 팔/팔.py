import sys
input = sys.stdin.readline

l, r = list(map(str, input().split()))

if len(l) == len(r):
    count = 0
    for i in range(len(l)):
        if l[i] != r[i]:
            break
        elif l[i] == '8':
            count += 1
    print(count)
else:
    print(0)