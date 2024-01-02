import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
pre = [0]

for i in range(1, n+1):
    pre.append(pre[i-1] + num[i-1])

m = int(input())

for i in range(m):
    s, e = list(map(int, input().split()))
    print(pre[e] - pre[s-1])