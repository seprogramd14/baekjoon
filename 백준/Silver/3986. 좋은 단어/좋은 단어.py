import sys
input = sys.stdin.readline

n = int(input())
count = 0

for _ in range(n):
    stack = list()
    for s in input().rstrip():
        if not stack:
            stack.append(s)
        elif stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    if not stack:
        count += 1
print(count)