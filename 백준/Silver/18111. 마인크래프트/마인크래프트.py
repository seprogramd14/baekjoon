import sys
from collections import Counter
input = sys.stdin.readline

n,m,b = list(map(int, input().split()))
land = []
for _ in range(n): land += list(map(int, input().split()))

time = [0 for i in range(257)]
height = 0
for i in range(257):
	b_c = b
	for j in land:
		if j <= i:
			time[i] += i - j
			b_c -= i - j
		else:
			time[i] += 2 * (j - i)
			b_c += j - i
	if b_c >= 0 and time[i] <= time[height]:
		height = i

print(time[height], height)