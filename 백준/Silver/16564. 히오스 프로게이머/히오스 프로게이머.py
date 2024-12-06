import sys
input = sys.stdin.readline

n, k = map(int, input().split())
level = sorted([int(input()) for _  in range(n)])

start, end = level[0], level[-1] + k
result = 0
while start <= end:
    mid = (start+end) // 2
    t = 0

    for l in level:
        if mid >= l:
            t += mid - l

    if t > k:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)