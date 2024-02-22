import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
ls = [n // k] * k
for i in range(n % k):
    ls[i] += 1
result = 1
for i in range(k):
    result *= ls[i]
print(result)