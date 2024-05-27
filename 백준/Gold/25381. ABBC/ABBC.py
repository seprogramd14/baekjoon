import sys
from collections import deque
input = sys.stdin.readline

a, b, c = deque(), deque(), deque()
s = input().rstrip()
count = 0

for i in range(len(s)):
    if s[i] == 'A':
        a.append(i)
    elif s[i] == "B":
        b.append(i)
    elif b:
        b.popleft()
        count += 1

while a and b:
    if a[0] < b[0]:
        a.popleft()
        count += 1
    b.popleft()
print(count)