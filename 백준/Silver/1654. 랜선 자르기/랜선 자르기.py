import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
cables = sorted([int(input()) for _ in range(n)])

start = 1
end = max(cables)

while start <= end:
	mid = (start + end) // 2

	count = 0
	for cable in cables:
		count += cable // mid
	
	if count >= k:
		start = mid + 1
	else:
		end = mid - 1
	
print(end)