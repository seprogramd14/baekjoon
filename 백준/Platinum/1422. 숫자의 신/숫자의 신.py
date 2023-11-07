from functools import cmp_to_key
import sys
input = sys.stdin.readline
def compare(x, y):
    if x + y > y + x:
        return -1
    if x + y == y + x:
        return 0
    else:
        return 1

n, k = list(map(int, input().split()))
num = [int(input()) for _ in range(n)]
while k > len(num):
    num.append(max(num))
for i in range(len(num)):
    num[i] = str(num[i])
num.sort(key = cmp_to_key(compare))
print(''.join(num))