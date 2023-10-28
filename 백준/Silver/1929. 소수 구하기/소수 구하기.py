import sys
input = sys.stdin.readline

start, end = list(map(int, input().split()))
num = [i for i in range(2, end+1)]

for i in range(len(num)):
	if num[i] != 0:
		for j in range(i+num[i], len(num), num[i]):
			num[j] = 0

num = num[start-2:] if start != 1 else num[start-1:]
for i in num:
	if i != 0:
		print(i)