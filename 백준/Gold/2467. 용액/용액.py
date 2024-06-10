import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))

start, end = 0, n-1
result = abs(ls[start] + ls[end])
p1, p2 = 0, n-1
while start < end:
    mid = abs(ls[start] + ls[end])
    if mid <= result:
        result = mid
        p1, p2 = start, end
    if abs(ls[start+1] + ls[end]) > abs(ls[start] + ls[end-1]):
        end -= 1
    else:
        start += 1
print(ls[p1], ls[p2])