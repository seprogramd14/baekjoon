import sys
input = sys.stdin.readline

w, h = list(map(int, input().split()))
x, y = list(map(int, input().split()))
t = int(input())

twx, thy = t % (2*w)+x, t % (2*h)+y
if w < twx:
    twx = 2*w - twx
if twx < 0:
    twx = -twx
if h < thy:
    thy = 2*h - thy
if thy < 0:
    thy = -thy
print(twx, thy)