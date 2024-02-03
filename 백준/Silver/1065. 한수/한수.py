import sys
input = sys.stdin.readline

n = int(input())
count = n

for i in range(1, n+1):
    st = str(i)
    if len(st) > 2:
        start = int(st[0]) - int(st[1])
        for s in range(1, len(st)-1):
            if int(st[s]) - int(st[s+1]) != start:
                count -= 1
                break
print(count)