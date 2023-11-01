import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
trees = sorted(list(map(int, input().split())))

start = 1
end = sum(trees) - 1
while start <= end:
    mid = (start + end) // 2
    count = 0
    for tree in trees:
        if tree >= mid:
            count += tree - mid
    if count >= m:
        start = mid + 1
    elif count < m:
        end = mid - 1
print(end)