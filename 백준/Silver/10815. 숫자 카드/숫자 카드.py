import sys
input = sys.stdin.readline

n = int(input())
have = sorted(list(map(int, input().split())))
m = int(input())
card = list(map(int, input().split()))

result = []
for c in card:
    start, end, check = 0, n-1, 0
    while start <= end:
        mid = (start + end) // 2
        if have[mid] == c:
            check = 1
            break
        elif have[mid] > c:
            end = mid - 1
        else:
            start = mid + 1
    
    result.append(check)
print(*result)