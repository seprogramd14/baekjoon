import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))
ls = sorted([int(input()) for _ in range(n)])

start = 1
end = ls[-1] - ls[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    first = ls[0]
    answer = 1

    for i in range(1, n):
        if ls[i] - first >= mid:
            first = ls[i]
            answer += 1
    
    if answer < c:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)