import sys
input = sys.stdin.readline
n = int(input())
ls = sorted(list(map(int, input().split())))
value = 0
for i in range(1, n):
    value += ls[i] - ls[i-1]
print(value+ls[-1]-ls[0])