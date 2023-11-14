import sys
input = sys.stdin.readline
n = int(input())
stack = []

for i in range(n):
    cmd = list(map(int, input().rstrip().split()))
    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        print(0 if stack else 1)
    elif cmd[0] == 5:
        print(stack[-1] if stack else -1)