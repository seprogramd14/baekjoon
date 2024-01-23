import sys
input = sys.stdin.readline

n, b = list(map(str, input().rstrip().split()))
l, b = len(n) - 1, int(b)
result = 0

for s in n:
    if s.isdigit():
        result += int(s) * (b ** l)
    else:
        result += (ord(s) - ord('A') + 10) * (b ** l)
    l -= 1

print(result)