import sys
input = sys.stdin.readline

s, w = map(int, input().split())
button = [abs(int(input()) - w) for _ in range(int(input()))]

if abs(s-w) < min(button)+1:
    print(abs(s-w))
else:
    print(min(button)+1)