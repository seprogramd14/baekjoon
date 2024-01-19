import sys
input = sys.stdin.readline

x, y = list(map(int, input().split()))
z = int(y * 100 / x)
start = 1
end = 10**9 - 1
count = 0

if z >= 99:
    print(-1)
    exit()

while start <= end:
    mid = (start + end) // 2
    count = int((y+mid)*100 / (x+mid))
    if count > z:
        end = mid - 1
    else:
        start = mid + 1

print(start)