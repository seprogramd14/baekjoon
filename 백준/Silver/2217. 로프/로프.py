import sys
input = sys.stdin.readline

n = int(input())
rope = sorted([int(input()) for _ in range(n)], reverse=True)
res = []

for i in range(n):
    res.append(rope[-1]*(n-i))
    rope.pop()
print(max(res))