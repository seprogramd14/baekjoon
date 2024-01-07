import sys
input = sys.stdin.readline

n = int(input())
money = sorted(list(map(int, input().split())))
cut = int(input())

start = 1
end = money[-1] # 이거보단 작아야 함

while start <= end:
    mid = (start + end) // 2
    result = 0
    for m in money:
        if m > mid:
            result += mid
        else:
            result += m
    if result <= cut:
        start = mid + 1
    else:
        end = mid - 1
print(end) # mid 말고 end