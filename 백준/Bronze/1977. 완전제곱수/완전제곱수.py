import sys
input = sys.stdin.readline

first, end = (int(input()) for _ in range(2))
result = []
for i in range(1, 101):
    num = i**2
    if first <= num <= end:
        result.append(num)

if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
