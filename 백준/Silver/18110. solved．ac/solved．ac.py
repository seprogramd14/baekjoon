import sys
input = sys.stdin.readline

def _round(n): # python round()는 오사오입 (0.5 앞이 짝수면 버림, 홀수면 올림)
	if n - int(n) >= 0.5:
		return int(n) + 1
	else:
		return int(n)
	return

n = int(input())
if n != 0:
	trim = _round((n * 3) / 20)

	diff = [int(input()) for i in range(n)]
	diff.sort()

	diff = diff[trim:len(diff)-trim]

	print(_round(sum(diff) / len(diff)))
else:
	print(0)