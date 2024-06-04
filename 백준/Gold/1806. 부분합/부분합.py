import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))
p = [0]
for i in ls:
    p.append(p[-1] + i)

start, end = 0, 1
length = float('inf')
while end <= n: # p는 인덱스가 하나 더 있다.
    if p[end] - p[start] < k:
        end += 1
    else:
        if length > end - start:
            length = end - start
        start += 1

if p[-1] < k:
    print(0)
else:
    print(length)